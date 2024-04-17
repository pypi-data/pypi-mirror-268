"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._661 import ActiveProcessMethod
    from ._662 import AnalysisMethod
    from ._663 import CalculateLeadDeviationAccuracy
    from ._664 import CalculatePitchDeviationAccuracy
    from ._665 import CalculateProfileDeviationAccuracy
    from ._666 import CentreDistanceOffsetMethod
    from ._667 import CutterHeadSlideError
    from ._668 import GearMountingError
    from ._669 import HobbingProcessCalculation
    from ._670 import HobbingProcessGearShape
    from ._671 import HobbingProcessLeadCalculation
    from ._672 import HobbingProcessMarkOnShaft
    from ._673 import HobbingProcessPitchCalculation
    from ._674 import HobbingProcessProfileCalculation
    from ._675 import HobbingProcessSimulationInput
    from ._676 import HobbingProcessSimulationNew
    from ._677 import HobbingProcessSimulationViewModel
    from ._678 import HobbingProcessTotalModificationCalculation
    from ._679 import HobManufactureError
    from ._680 import HobResharpeningError
    from ._681 import ManufacturedQualityGrade
    from ._682 import MountingError
    from ._683 import ProcessCalculation
    from ._684 import ProcessGearShape
    from ._685 import ProcessLeadCalculation
    from ._686 import ProcessPitchCalculation
    from ._687 import ProcessProfileCalculation
    from ._688 import ProcessSimulationInput
    from ._689 import ProcessSimulationNew
    from ._690 import ProcessSimulationViewModel
    from ._691 import ProcessTotalModificationCalculation
    from ._692 import RackManufactureError
    from ._693 import RackMountingError
    from ._694 import WormGrinderManufactureError
    from ._695 import WormGrindingCutterCalculation
    from ._696 import WormGrindingLeadCalculation
    from ._697 import WormGrindingProcessCalculation
    from ._698 import WormGrindingProcessGearShape
    from ._699 import WormGrindingProcessMarkOnShaft
    from ._700 import WormGrindingProcessPitchCalculation
    from ._701 import WormGrindingProcessProfileCalculation
    from ._702 import WormGrindingProcessSimulationInput
    from ._703 import WormGrindingProcessSimulationNew
    from ._704 import WormGrindingProcessSimulationViewModel
    from ._705 import WormGrindingProcessTotalModificationCalculation
else:
    import_structure = {
        "_661": ["ActiveProcessMethod"],
        "_662": ["AnalysisMethod"],
        "_663": ["CalculateLeadDeviationAccuracy"],
        "_664": ["CalculatePitchDeviationAccuracy"],
        "_665": ["CalculateProfileDeviationAccuracy"],
        "_666": ["CentreDistanceOffsetMethod"],
        "_667": ["CutterHeadSlideError"],
        "_668": ["GearMountingError"],
        "_669": ["HobbingProcessCalculation"],
        "_670": ["HobbingProcessGearShape"],
        "_671": ["HobbingProcessLeadCalculation"],
        "_672": ["HobbingProcessMarkOnShaft"],
        "_673": ["HobbingProcessPitchCalculation"],
        "_674": ["HobbingProcessProfileCalculation"],
        "_675": ["HobbingProcessSimulationInput"],
        "_676": ["HobbingProcessSimulationNew"],
        "_677": ["HobbingProcessSimulationViewModel"],
        "_678": ["HobbingProcessTotalModificationCalculation"],
        "_679": ["HobManufactureError"],
        "_680": ["HobResharpeningError"],
        "_681": ["ManufacturedQualityGrade"],
        "_682": ["MountingError"],
        "_683": ["ProcessCalculation"],
        "_684": ["ProcessGearShape"],
        "_685": ["ProcessLeadCalculation"],
        "_686": ["ProcessPitchCalculation"],
        "_687": ["ProcessProfileCalculation"],
        "_688": ["ProcessSimulationInput"],
        "_689": ["ProcessSimulationNew"],
        "_690": ["ProcessSimulationViewModel"],
        "_691": ["ProcessTotalModificationCalculation"],
        "_692": ["RackManufactureError"],
        "_693": ["RackMountingError"],
        "_694": ["WormGrinderManufactureError"],
        "_695": ["WormGrindingCutterCalculation"],
        "_696": ["WormGrindingLeadCalculation"],
        "_697": ["WormGrindingProcessCalculation"],
        "_698": ["WormGrindingProcessGearShape"],
        "_699": ["WormGrindingProcessMarkOnShaft"],
        "_700": ["WormGrindingProcessPitchCalculation"],
        "_701": ["WormGrindingProcessProfileCalculation"],
        "_702": ["WormGrindingProcessSimulationInput"],
        "_703": ["WormGrindingProcessSimulationNew"],
        "_704": ["WormGrindingProcessSimulationViewModel"],
        "_705": ["WormGrindingProcessTotalModificationCalculation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProcessMethod",
    "AnalysisMethod",
    "CalculateLeadDeviationAccuracy",
    "CalculatePitchDeviationAccuracy",
    "CalculateProfileDeviationAccuracy",
    "CentreDistanceOffsetMethod",
    "CutterHeadSlideError",
    "GearMountingError",
    "HobbingProcessCalculation",
    "HobbingProcessGearShape",
    "HobbingProcessLeadCalculation",
    "HobbingProcessMarkOnShaft",
    "HobbingProcessPitchCalculation",
    "HobbingProcessProfileCalculation",
    "HobbingProcessSimulationInput",
    "HobbingProcessSimulationNew",
    "HobbingProcessSimulationViewModel",
    "HobbingProcessTotalModificationCalculation",
    "HobManufactureError",
    "HobResharpeningError",
    "ManufacturedQualityGrade",
    "MountingError",
    "ProcessCalculation",
    "ProcessGearShape",
    "ProcessLeadCalculation",
    "ProcessPitchCalculation",
    "ProcessProfileCalculation",
    "ProcessSimulationInput",
    "ProcessSimulationNew",
    "ProcessSimulationViewModel",
    "ProcessTotalModificationCalculation",
    "RackManufactureError",
    "RackMountingError",
    "WormGrinderManufactureError",
    "WormGrindingCutterCalculation",
    "WormGrindingLeadCalculation",
    "WormGrindingProcessCalculation",
    "WormGrindingProcessGearShape",
    "WormGrindingProcessMarkOnShaft",
    "WormGrindingProcessPitchCalculation",
    "WormGrindingProcessProfileCalculation",
    "WormGrindingProcessSimulationInput",
    "WormGrindingProcessSimulationNew",
    "WormGrindingProcessSimulationViewModel",
    "WormGrindingProcessTotalModificationCalculation",
)
