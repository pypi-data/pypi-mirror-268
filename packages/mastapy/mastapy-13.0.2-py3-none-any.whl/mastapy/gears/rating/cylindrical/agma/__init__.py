"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._537 import AGMA2101GearSingleFlankRating
    from ._538 import AGMA2101MeshSingleFlankRating
    from ._539 import AGMA2101RateableMesh
    from ._540 import ThermalReductionFactorFactorsAndExponents
else:
    import_structure = {
        "_537": ["AGMA2101GearSingleFlankRating"],
        "_538": ["AGMA2101MeshSingleFlankRating"],
        "_539": ["AGMA2101RateableMesh"],
        "_540": ["ThermalReductionFactorFactorsAndExponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2101GearSingleFlankRating",
    "AGMA2101MeshSingleFlankRating",
    "AGMA2101RateableMesh",
    "ThermalReductionFactorFactorsAndExponents",
)
