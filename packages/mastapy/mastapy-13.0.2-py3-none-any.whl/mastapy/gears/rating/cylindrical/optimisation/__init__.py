"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._504 import CylindricalGearSetRatingOptimisationHelper
    from ._505 import OptimisationResultsPair
    from ._506 import SafetyFactorOptimisationResults
    from ._507 import SafetyFactorOptimisationStepResult
    from ._508 import SafetyFactorOptimisationStepResultAngle
    from ._509 import SafetyFactorOptimisationStepResultNumber
    from ._510 import SafetyFactorOptimisationStepResultShortLength
else:
    import_structure = {
        "_504": ["CylindricalGearSetRatingOptimisationHelper"],
        "_505": ["OptimisationResultsPair"],
        "_506": ["SafetyFactorOptimisationResults"],
        "_507": ["SafetyFactorOptimisationStepResult"],
        "_508": ["SafetyFactorOptimisationStepResultAngle"],
        "_509": ["SafetyFactorOptimisationStepResultNumber"],
        "_510": ["SafetyFactorOptimisationStepResultShortLength"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearSetRatingOptimisationHelper",
    "OptimisationResultsPair",
    "SafetyFactorOptimisationResults",
    "SafetyFactorOptimisationStepResult",
    "SafetyFactorOptimisationStepResultAngle",
    "SafetyFactorOptimisationStepResultNumber",
    "SafetyFactorOptimisationStepResultShortLength",
)
