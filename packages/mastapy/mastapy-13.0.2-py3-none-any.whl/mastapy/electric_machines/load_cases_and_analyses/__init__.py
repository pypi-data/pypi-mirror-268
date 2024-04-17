"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1353 import BasicDynamicForceLoadCase
    from ._1354 import DynamicForceAnalysis
    from ._1355 import DynamicForceLoadCase
    from ._1356 import DynamicForcesOperatingPoint
    from ._1357 import EfficiencyMapAnalysis
    from ._1358 import EfficiencyMapLoadCase
    from ._1359 import ElectricMachineAnalysis
    from ._1360 import ElectricMachineBasicMechanicalLossSettings
    from ._1361 import ElectricMachineControlStrategy
    from ._1362 import ElectricMachineEfficiencyMapSettings
    from ._1363 import ElectricMachineFEAnalysis
    from ._1364 import ElectricMachineFEMechanicalAnalysis
    from ._1365 import ElectricMachineLoadCase
    from ._1366 import ElectricMachineLoadCaseBase
    from ._1367 import ElectricMachineLoadCaseGroup
    from ._1368 import ElectricMachineMechanicalLoadCase
    from ._1369 import EndWindingInductanceMethod
    from ._1370 import LeadingOrLagging
    from ._1371 import LoadCaseType
    from ._1372 import LoadCaseTypeSelector
    from ._1373 import MotoringOrGenerating
    from ._1374 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1375 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1376 import OperatingPointsSpecificationMethod
    from ._1377 import SingleOperatingPointAnalysis
    from ._1378 import SlotDetailForAnalysis
    from ._1379 import SpecifyTorqueOrCurrent
    from ._1380 import SpeedPointsDistribution
    from ._1381 import SpeedTorqueCurveAnalysis
    from ._1382 import SpeedTorqueCurveLoadCase
    from ._1383 import SpeedTorqueLoadCase
    from ._1384 import Temperatures
else:
    import_structure = {
        "_1353": ["BasicDynamicForceLoadCase"],
        "_1354": ["DynamicForceAnalysis"],
        "_1355": ["DynamicForceLoadCase"],
        "_1356": ["DynamicForcesOperatingPoint"],
        "_1357": ["EfficiencyMapAnalysis"],
        "_1358": ["EfficiencyMapLoadCase"],
        "_1359": ["ElectricMachineAnalysis"],
        "_1360": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1361": ["ElectricMachineControlStrategy"],
        "_1362": ["ElectricMachineEfficiencyMapSettings"],
        "_1363": ["ElectricMachineFEAnalysis"],
        "_1364": ["ElectricMachineFEMechanicalAnalysis"],
        "_1365": ["ElectricMachineLoadCase"],
        "_1366": ["ElectricMachineLoadCaseBase"],
        "_1367": ["ElectricMachineLoadCaseGroup"],
        "_1368": ["ElectricMachineMechanicalLoadCase"],
        "_1369": ["EndWindingInductanceMethod"],
        "_1370": ["LeadingOrLagging"],
        "_1371": ["LoadCaseType"],
        "_1372": ["LoadCaseTypeSelector"],
        "_1373": ["MotoringOrGenerating"],
        "_1374": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1375": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1376": ["OperatingPointsSpecificationMethod"],
        "_1377": ["SingleOperatingPointAnalysis"],
        "_1378": ["SlotDetailForAnalysis"],
        "_1379": ["SpecifyTorqueOrCurrent"],
        "_1380": ["SpeedPointsDistribution"],
        "_1381": ["SpeedTorqueCurveAnalysis"],
        "_1382": ["SpeedTorqueCurveLoadCase"],
        "_1383": ["SpeedTorqueLoadCase"],
        "_1384": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
