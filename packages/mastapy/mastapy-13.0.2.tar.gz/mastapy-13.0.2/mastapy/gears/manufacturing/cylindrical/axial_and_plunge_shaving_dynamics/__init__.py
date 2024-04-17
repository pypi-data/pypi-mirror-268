"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._752 import ActiveProfileRangeCalculationSource
    from ._753 import AxialShaverRedressing
    from ._754 import ConventionalShavingDynamics
    from ._755 import ConventionalShavingDynamicsCalculationForDesignedGears
    from ._756 import ConventionalShavingDynamicsCalculationForHobbedGears
    from ._757 import ConventionalShavingDynamicsViewModel
    from ._758 import PlungeShaverDynamics
    from ._759 import PlungeShaverDynamicSettings
    from ._760 import PlungeShaverRedressing
    from ._761 import PlungeShavingDynamicsCalculationForDesignedGears
    from ._762 import PlungeShavingDynamicsCalculationForHobbedGears
    from ._763 import PlungeShavingDynamicsViewModel
    from ._764 import RedressingSettings
    from ._765 import RollAngleRangeRelativeToAccuracy
    from ._766 import RollAngleReportObject
    from ._767 import ShaverRedressing
    from ._768 import ShavingDynamics
    from ._769 import ShavingDynamicsCalculation
    from ._770 import ShavingDynamicsCalculationForDesignedGears
    from ._771 import ShavingDynamicsCalculationForHobbedGears
    from ._772 import ShavingDynamicsConfiguration
    from ._773 import ShavingDynamicsViewModel
    from ._774 import ShavingDynamicsViewModelBase
else:
    import_structure = {
        "_752": ["ActiveProfileRangeCalculationSource"],
        "_753": ["AxialShaverRedressing"],
        "_754": ["ConventionalShavingDynamics"],
        "_755": ["ConventionalShavingDynamicsCalculationForDesignedGears"],
        "_756": ["ConventionalShavingDynamicsCalculationForHobbedGears"],
        "_757": ["ConventionalShavingDynamicsViewModel"],
        "_758": ["PlungeShaverDynamics"],
        "_759": ["PlungeShaverDynamicSettings"],
        "_760": ["PlungeShaverRedressing"],
        "_761": ["PlungeShavingDynamicsCalculationForDesignedGears"],
        "_762": ["PlungeShavingDynamicsCalculationForHobbedGears"],
        "_763": ["PlungeShavingDynamicsViewModel"],
        "_764": ["RedressingSettings"],
        "_765": ["RollAngleRangeRelativeToAccuracy"],
        "_766": ["RollAngleReportObject"],
        "_767": ["ShaverRedressing"],
        "_768": ["ShavingDynamics"],
        "_769": ["ShavingDynamicsCalculation"],
        "_770": ["ShavingDynamicsCalculationForDesignedGears"],
        "_771": ["ShavingDynamicsCalculationForHobbedGears"],
        "_772": ["ShavingDynamicsConfiguration"],
        "_773": ["ShavingDynamicsViewModel"],
        "_774": ["ShavingDynamicsViewModelBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProfileRangeCalculationSource",
    "AxialShaverRedressing",
    "ConventionalShavingDynamics",
    "ConventionalShavingDynamicsCalculationForDesignedGears",
    "ConventionalShavingDynamicsCalculationForHobbedGears",
    "ConventionalShavingDynamicsViewModel",
    "PlungeShaverDynamics",
    "PlungeShaverDynamicSettings",
    "PlungeShaverRedressing",
    "PlungeShavingDynamicsCalculationForDesignedGears",
    "PlungeShavingDynamicsCalculationForHobbedGears",
    "PlungeShavingDynamicsViewModel",
    "RedressingSettings",
    "RollAngleRangeRelativeToAccuracy",
    "RollAngleReportObject",
    "ShaverRedressing",
    "ShavingDynamics",
    "ShavingDynamicsCalculation",
    "ShavingDynamicsCalculationForDesignedGears",
    "ShavingDynamicsCalculationForHobbedGears",
    "ShavingDynamicsConfiguration",
    "ShavingDynamicsViewModel",
    "ShavingDynamicsViewModelBase",
)
