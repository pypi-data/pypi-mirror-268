"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1795 import CellValuePosition
    from ._1796 import CustomChartType
else:
    import_structure = {
        "_1795": ["CellValuePosition"],
        "_1796": ["CustomChartType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CellValuePosition",
    "CustomChartType",
)
