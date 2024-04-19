"""Fedinesia - deletes old statuses from fediverse accounts. This tool was previously
called MastodonAmnesia
Copyright (C) 2021, 2022, 2023  Mark S Burgunder.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import asyncio
import json
import sys
from datetime import datetime
from datetime import timedelta
from math import ceil
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import msgspec
import stamina
import typer
from dateutil.parser import isoparse
from httpx import AsyncClient
from httpx import HTTPError
from loguru import logger as log
from minimal_activitypub.client_2_server import ActivityPub
from minimal_activitypub.client_2_server import ActivityPubError
from minimal_activitypub.client_2_server import NetworkError
from minimal_activitypub.client_2_server import NotFoundError
from minimal_activitypub.client_2_server import RatelimitError
from stamina import retry_context
from tqdm import tqdm
from tqdm import trange
from typing_extensions import Annotated

from fedinesia import UTC
from fedinesia import Status
from fedinesia import __display_name__
from fedinesia import __version__
from fedinesia.config import setup_shop
from fedinesia.util import AuditLog
from fedinesia.util import should_keep

logging_config_path = Path("logging-config.toml")
if logging_config_path.exists():
    with logging_config_path.open(mode="rb") as log_config_file:
        logging_config = msgspec.toml.decode(log_config_file.read())

    for handler in logging_config.get("handlers"):
        if handler.get("sink") == "sys.stdout":
            handler["sink"] = sys.stdout

    log.configure(**logging_config)

stamina.instrumentation.set_on_retry_hooks([])


@log.catch
async def main(  # noqa: C901, PLR0912, PLR0915
    config_file: str,
    is_dry_run: bool,
    audit_log_file: Optional[str],
    audit_log_style: Optional[AuditLog.Style],
    limit: Optional[int],
) -> None:
    """Perform app function."""
    config = await setup_shop(config_file=config_file)

    oldest_to_keep = datetime.now(tz=UTC) - timedelta(seconds=config.bot.delete_after)

    log.info(f"Welcome to {__display_name__} {__version__}")
    log.debug(f"{config=}")

    try:
        client = AsyncClient(http2=True)

        instance = ActivityPub(
            instance=config.mastodon.instance,
            access_token=config.mastodon.access_token,
            client=client,
        )
        await instance.determine_instance_type()
        user_info = await instance.verify_credentials()
        log.opt(colors=True).info(
            f"We are removing statuses older than <cyan>{oldest_to_keep}</> "
            f"from <cyan>{config.mastodon.instance}@{user_info['username']}</>"
        )

        audit_log = None
        if audit_log_file:
            log.info(f"A record of all deleted statuses will be recorded in the audit log file at {audit_log_file}")
            audit_log = AuditLog.open(audit_log_file=audit_log_file, style=audit_log_style)

        for attempt in retry_context(on=NetworkError, attempts=3):
            with attempt:
                statuses = await instance.get_account_statuses(account_id=user_info["id"])
    except RatelimitError:
        log.info(
            f"RateLimited during startup, [red]Please wait until[/red] {instance.ratelimit_reset} before trying again"
        )
        sys.exit(429)
    except (HTTPError, ActivityPubError):
        log.exception("!!! Cannot continue.")
        sys.exit(100)

    statuses_to_delete: List[Status] = []
    title = "Finding statuses to delete"
    progress_bar = tqdm(
        desc=f"{title:.<60}",
        ncols=120,
        unit="statuses",
        position=0,
        bar_format="{l_bar} {n_fmt} at {rate_fmt}",
    )
    while True:
        try:
            for status in statuses:
                log.debug(f"Processing status: {status.get('url')} " f"from {isoparse(status.get('created_at'))}")
                log.debug(
                    f"Oldest to keep vs status created at " f"{oldest_to_keep} > {isoparse(status.get('created_at'))}"
                )

                if should_keep(
                    status=status,
                    oldest_to_keep=oldest_to_keep,
                    config=config,
                ):
                    log.debug(
                        f"Not deleting status: "
                        f"Bookmarked: {status.get('bookmarked')} - "
                        f"My Fav: {status.get('favourited')} - "
                        f"Pinned: {status.get('pinned')} - "
                        f"Poll: {(status.get('poll') is not None)} - "
                        f"Attachments: {len(status.get('media_attachments'))} - "
                        f"Faved: {status.get('favourites_count')} - "
                        f"Boosted: {status.get('reblogs_count')} - "
                        f"Visibility: {status.get('visibility')} -+- "
                        f"Created At: {isoparse(status.get('created_at'))} -+- "
                        f"{status.get('url')}"
                    )

                elif limit and len(statuses_to_delete) >= limit:
                    break

                else:
                    statuses_to_delete.append(status)

                progress_bar.update()

            if limit and len(statuses_to_delete) >= limit:
                break

            # Get More statuses if available:
            log.debug("get next batch of statuses if available.")
            log.debug(f"{instance.pagination=}")
            if instance.pagination["next"]["max_id"] or instance.pagination["next"]["min_id"]:
                for attempt in retry_context(on=NetworkError):
                    with attempt:
                        statuses = await instance.get_account_statuses(
                            account_id=user_info["id"],
                            max_id=instance.pagination["next"]["max_id"],
                            min_id=instance.pagination["next"]["min_id"],
                        )
                log.debug(f"scrolling - {len(statuses)=}")
                if len(statuses) == 0:
                    break
            else:
                break

        except RatelimitError:
            await sleep_off_ratelimiting(instance=instance)

    progress_bar.close()

    total_statuses_to_delete = len(statuses_to_delete)
    log.debug(f"start deleting - {total_statuses_to_delete=}")
    for status in statuses_to_delete:
        log.debug(f"Start of deleting - status to delete: {status['id']} @ {status['url']}")

    # If dry-run has been specified, print out list of statuses that would be deleted
    if is_dry_run:
        log.opt(colors=True).info("F--dry-run or -d specified. <yellow><bold>No statuses will be deleted</></>")
        for status in statuses_to_delete:
            log.opt(colors=True).info(
                f"<red>Would</red> delete status" f" {status.get('url')} from {status.get('created_at')}"
            )
        log.opt(colors=True).info(f"<bold>Total of {total_statuses_to_delete} statuses would be deleted.</>")

    # Dry-run has not been specified... delete statuses!
    else:
        await delete_statuses(instance=instance, statuses_to_delete=statuses_to_delete, audit=audit_log)
        log.info(f"All old statuses deleted! Total of {total_statuses_to_delete} statuses deleted")

    if audit_log:
        audit_log.close()
    await client.aclose()


async def delete_statuses(instance: ActivityPub, statuses_to_delete: List[Status], audit: Optional[AuditLog]) -> None:
    """Delete all statuses that should be deleted."""
    title = "Deleting statuses"
    total_statuses_to_delete = len(statuses_to_delete)
    for status in tqdm(
        iterable=statuses_to_delete,
        desc=f"{title:.<60}",
        ncols=120,
        total=total_statuses_to_delete,
        unit="statuses",
        position=0,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} at {rate_fmt}",
    ):
        try:
            for attempt in retry_context(on=NetworkError):
                with attempt:
                    await delete_single_status(status=status, instance=instance, audit=audit)
        except RatelimitError:
            await sleep_off_ratelimiting(instance=instance)


async def sleep_off_ratelimiting(
    instance: ActivityPub,
) -> None:
    """Wait for rate limiting to be over."""
    log.debug(
        f"sleep_off_ratelimiting - Rate limited: Limit: {instance.ratelimit_remaining} - "
        f"resetting at: {instance.ratelimit_reset}"
    )
    now = datetime.now(tz=UTC)
    need_to_wait = ceil((instance.ratelimit_reset - now).total_seconds())

    bar_title = f"Waiting until {instance.ratelimit_reset:%H:%M:%S %Z} to let server 'cool-down'"
    for _i in trange(
        need_to_wait,
        desc=f"{bar_title:.<60}",
        unit="s",
        ncols=120,
        bar_format="{desc}: {percentage:3.0f}%|{bar}| Eta: {remaining} - Elapsed: {elapsed}",
        position=1,
    ):
        await asyncio.sleep(1)


async def delete_single_status(
    status: Status,
    instance: ActivityPub,
    audit: Optional[AuditLog],
) -> Optional[Dict[str, Any]]:
    """Delete  single status."""
    log.debug(f"delete_single_status(status={status['id']}, instance={instance.instance})")
    return_status: Optional[Status] = status
    try:
        await instance.delete_status(status=status)
        log.debug(f"delete_single_status - Deleted status {status.get('url')} from {status.get('created_at')}")
        if audit:
            audit.add_entry(status=status)
    except NotFoundError:
        log.debug("Status for deletion not found. No problem then :)")
    except ActivityPubError as error:
        log.debug(f"delete_single_status - encountered error: {error}")
        log.debug(f"delete_single_status - status: {json.dumps(status, indent=4)}")
        raise error

    return return_status


def start() -> None:
    """Start app."""
    typer.run(typer_async_shim)


def typer_async_shim(
    config_file: Annotated[str, typer.Option("-c", "--config-file")] = "config.json",
    audit_log_file: Annotated[Optional[str], typer.Option("-a", "--audit-log-file")] = None,
    audit_log_style: Optional[AuditLog.Style] = AuditLog.Style.PLAIN,
    limit: Annotated[Optional[int], typer.Option("-l", "--limit")] = None,
    dry_run: Annotated[bool, typer.Option("-d", "--dry-run")] = False,
) -> None:
    """Delete fediverse history. For more information look at https://codeberg.org/MarvinsMastodonTools/fedinesia."""
    asyncio.run(
        main(
            config_file=config_file,
            is_dry_run=dry_run,
            audit_log_file=audit_log_file,
            audit_log_style=audit_log_style,
            limit=limit,
        )
    )
