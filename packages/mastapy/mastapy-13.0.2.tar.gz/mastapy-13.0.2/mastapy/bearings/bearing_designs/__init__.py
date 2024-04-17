"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2137 import BearingDesign
    from ._2138 import DetailedBearing
    from ._2139 import DummyRollingBearing
    from ._2140 import LinearBearing
    from ._2141 import NonLinearBearing
else:
    import_structure = {
        "_2137": ["BearingDesign"],
        "_2138": ["DetailedBearing"],
        "_2139": ["DummyRollingBearing"],
        "_2140": ["LinearBearing"],
        "_2141": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)
