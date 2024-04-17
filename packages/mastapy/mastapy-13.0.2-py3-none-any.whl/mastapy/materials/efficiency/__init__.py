"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._295 import BearingEfficiencyRatingMethod
    from ._296 import CombinedResistiveTorque
    from ._297 import EfficiencyRatingMethod
    from ._298 import IndependentPowerLoss
    from ._299 import IndependentResistiveTorque
    from ._300 import LoadAndSpeedCombinedPowerLoss
    from ._301 import OilPumpDetail
    from ._302 import OilPumpDriveType
    from ._303 import OilSealLossCalculationMethod
    from ._304 import OilSealMaterialType
    from ._305 import PowerLoss
    from ._306 import ResistiveTorque
else:
    import_structure = {
        "_295": ["BearingEfficiencyRatingMethod"],
        "_296": ["CombinedResistiveTorque"],
        "_297": ["EfficiencyRatingMethod"],
        "_298": ["IndependentPowerLoss"],
        "_299": ["IndependentResistiveTorque"],
        "_300": ["LoadAndSpeedCombinedPowerLoss"],
        "_301": ["OilPumpDetail"],
        "_302": ["OilPumpDriveType"],
        "_303": ["OilSealLossCalculationMethod"],
        "_304": ["OilSealMaterialType"],
        "_305": ["PowerLoss"],
        "_306": ["ResistiveTorque"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingEfficiencyRatingMethod",
    "CombinedResistiveTorque",
    "EfficiencyRatingMethod",
    "IndependentPowerLoss",
    "IndependentResistiveTorque",
    "LoadAndSpeedCombinedPowerLoss",
    "OilPumpDetail",
    "OilPumpDriveType",
    "OilSealLossCalculationMethod",
    "OilSealMaterialType",
    "PowerLoss",
    "ResistiveTorque",
)
