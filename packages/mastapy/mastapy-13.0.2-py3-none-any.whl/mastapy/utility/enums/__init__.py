"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1826 import BearingForceArrowOption
    from ._1827 import TableAndChartOptions
    from ._1828 import ThreeDViewContourOption
    from ._1829 import ThreeDViewContourOptionFirstSelection
    from ._1830 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1826": ["BearingForceArrowOption"],
        "_1827": ["TableAndChartOptions"],
        "_1828": ["ThreeDViewContourOption"],
        "_1829": ["ThreeDViewContourOptionFirstSelection"],
        "_1830": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
