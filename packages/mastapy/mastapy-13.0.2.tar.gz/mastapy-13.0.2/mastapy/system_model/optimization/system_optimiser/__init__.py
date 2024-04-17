"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2244 import DesignStateTargetRatio
    from ._2245 import PlanetGearOptions
    from ._2246 import SystemOptimiser
    from ._2247 import SystemOptimiserDetails
    from ._2248 import ToothNumberFinder
else:
    import_structure = {
        "_2244": ["DesignStateTargetRatio"],
        "_2245": ["PlanetGearOptions"],
        "_2246": ["SystemOptimiser"],
        "_2247": ["SystemOptimiserDetails"],
        "_2248": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)
