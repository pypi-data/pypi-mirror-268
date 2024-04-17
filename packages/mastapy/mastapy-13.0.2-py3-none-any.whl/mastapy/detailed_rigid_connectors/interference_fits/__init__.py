"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1450 import AssemblyMethods
    from ._1451 import CalculationMethods
    from ._1452 import InterferenceFitDesign
    from ._1453 import InterferenceFitHalfDesign
    from ._1454 import StressRegions
    from ._1455 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1450": ["AssemblyMethods"],
        "_1451": ["CalculationMethods"],
        "_1452": ["InterferenceFitDesign"],
        "_1453": ["InterferenceFitHalfDesign"],
        "_1454": ["StressRegions"],
        "_1455": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
