"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1798 import Fix
    from ._1799 import Severity
    from ._1800 import Status
    from ._1801 import StatusItem
    from ._1802 import StatusItemSeverity
else:
    import_structure = {
        "_1798": ["Fix"],
        "_1799": ["Severity"],
        "_1800": ["Status"],
        "_1801": ["StatusItem"],
        "_1802": ["StatusItemSeverity"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
)
