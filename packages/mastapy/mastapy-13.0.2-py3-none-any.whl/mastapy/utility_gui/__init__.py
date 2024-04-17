"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1854 import ColumnInputOptions
    from ._1855 import DataInputFileOptions
    from ._1856 import DataLoggerItem
    from ._1857 import DataLoggerWithCharts
    from ._1858 import ScalingDrawStyle
else:
    import_structure = {
        "_1854": ["ColumnInputOptions"],
        "_1855": ["DataInputFileOptions"],
        "_1856": ["DataLoggerItem"],
        "_1857": ["DataLoggerWithCharts"],
        "_1858": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)
