"""Package 'fedinesia' level definitions."""

import sys
from datetime import timedelta
from datetime import timezone
from importlib.metadata import version
from typing import Any
from typing import Dict
from typing import Final

__version__: Final[str] = version(__package__)

__package_name__: Final[str] = __package__
__display_name__: Final[str] = __package__.title()
USER_AGENT: Final[str] = f"{__display_name__}_v{__version__}_Python_{sys.version.split()[0]}"

CLIENT_WEBSITE: Final[str] = "https://codeberg.org/MarvinsMastodonTools/fedinesia"

UTC = timezone(offset=timedelta(hours=0))

Status = Dict[str, Any]
