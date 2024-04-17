"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1328 import DynamicForceResults
    from ._1329 import EfficiencyResults
    from ._1330 import ElectricMachineDQModel
    from ._1331 import ElectricMachineMechanicalResults
    from ._1332 import ElectricMachineMechanicalResultsViewable
    from ._1333 import ElectricMachineResults
    from ._1334 import ElectricMachineResultsForConductorTurn
    from ._1335 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1336 import ElectricMachineResultsForLineToLine
    from ._1337 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1338 import ElectricMachineResultsForPhase
    from ._1339 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1340 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1341 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1342 import ElectricMachineResultsTimeStep
    from ._1343 import ElectricMachineResultsTimeStepAtLocation
    from ._1344 import ElectricMachineResultsViewable
    from ._1345 import ElectricMachineForceViewOptions
    from ._1347 import LinearDQModel
    from ._1348 import MaximumTorqueResultsPoints
    from ._1349 import NonLinearDQModel
    from ._1350 import NonLinearDQModelGeneratorSettings
    from ._1351 import OnLoadElectricMachineResults
    from ._1352 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1328": ["DynamicForceResults"],
        "_1329": ["EfficiencyResults"],
        "_1330": ["ElectricMachineDQModel"],
        "_1331": ["ElectricMachineMechanicalResults"],
        "_1332": ["ElectricMachineMechanicalResultsViewable"],
        "_1333": ["ElectricMachineResults"],
        "_1334": ["ElectricMachineResultsForConductorTurn"],
        "_1335": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1336": ["ElectricMachineResultsForLineToLine"],
        "_1337": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1338": ["ElectricMachineResultsForPhase"],
        "_1339": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1340": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1341": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1342": ["ElectricMachineResultsTimeStep"],
        "_1343": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1344": ["ElectricMachineResultsViewable"],
        "_1345": ["ElectricMachineForceViewOptions"],
        "_1347": ["LinearDQModel"],
        "_1348": ["MaximumTorqueResultsPoints"],
        "_1349": ["NonLinearDQModel"],
        "_1350": ["NonLinearDQModelGeneratorSettings"],
        "_1351": ["OnLoadElectricMachineResults"],
        "_1352": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
