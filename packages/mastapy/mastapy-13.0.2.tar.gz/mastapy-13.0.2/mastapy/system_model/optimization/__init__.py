"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2233 import ConicalGearOptimisationStrategy
    from ._2234 import ConicalGearOptimizationStep
    from ._2235 import ConicalGearOptimizationStrategyDatabase
    from ._2236 import CylindricalGearOptimisationStrategy
    from ._2237 import CylindricalGearOptimizationStep
    from ._2238 import MeasuredAndFactorViewModel
    from ._2239 import MicroGeometryOptimisationTarget
    from ._2240 import OptimizationStep
    from ._2241 import OptimizationStrategy
    from ._2242 import OptimizationStrategyBase
    from ._2243 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2233": ["ConicalGearOptimisationStrategy"],
        "_2234": ["ConicalGearOptimizationStep"],
        "_2235": ["ConicalGearOptimizationStrategyDatabase"],
        "_2236": ["CylindricalGearOptimisationStrategy"],
        "_2237": ["CylindricalGearOptimizationStep"],
        "_2238": ["MeasuredAndFactorViewModel"],
        "_2239": ["MicroGeometryOptimisationTarget"],
        "_2240": ["OptimizationStep"],
        "_2241": ["OptimizationStrategy"],
        "_2242": ["OptimizationStrategyBase"],
        "_2243": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
