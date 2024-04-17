"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._775 import AbstractTCA
    from ._776 import BevelMachineSettingOptimizationResult
    from ._777 import ConicalFlankDeviationsData
    from ._778 import ConicalGearManufacturingAnalysis
    from ._779 import ConicalGearManufacturingConfig
    from ._780 import ConicalGearMicroGeometryConfig
    from ._781 import ConicalGearMicroGeometryConfigBase
    from ._782 import ConicalMeshedGearManufacturingAnalysis
    from ._783 import ConicalMeshedWheelFlankManufacturingConfig
    from ._784 import ConicalMeshFlankManufacturingConfig
    from ._785 import ConicalMeshFlankMicroGeometryConfig
    from ._786 import ConicalMeshFlankNURBSMicroGeometryConfig
    from ._787 import ConicalMeshManufacturingAnalysis
    from ._788 import ConicalMeshManufacturingConfig
    from ._789 import ConicalMeshMicroGeometryConfig
    from ._790 import ConicalMeshMicroGeometryConfigBase
    from ._791 import ConicalPinionManufacturingConfig
    from ._792 import ConicalPinionMicroGeometryConfig
    from ._793 import ConicalSetManufacturingAnalysis
    from ._794 import ConicalSetManufacturingConfig
    from ._795 import ConicalSetMicroGeometryConfig
    from ._796 import ConicalSetMicroGeometryConfigBase
    from ._797 import ConicalWheelManufacturingConfig
    from ._798 import EaseOffBasedTCA
    from ._799 import FlankMeasurementBorder
    from ._800 import HypoidAdvancedLibrary
    from ._801 import MachineTypes
    from ._802 import ManufacturingMachine
    from ._803 import ManufacturingMachineDatabase
    from ._804 import PinionBevelGeneratingModifiedRollMachineSettings
    from ._805 import PinionBevelGeneratingTiltMachineSettings
    from ._806 import PinionConcave
    from ._807 import PinionConicalMachineSettingsSpecified
    from ._808 import PinionConvex
    from ._809 import PinionFinishMachineSettings
    from ._810 import PinionHypoidFormateTiltMachineSettings
    from ._811 import PinionHypoidGeneratingTiltMachineSettings
    from ._812 import PinionMachineSettingsSMT
    from ._813 import PinionRoughMachineSetting
    from ._814 import Wheel
    from ._815 import WheelFormatMachineTypes
else:
    import_structure = {
        "_775": ["AbstractTCA"],
        "_776": ["BevelMachineSettingOptimizationResult"],
        "_777": ["ConicalFlankDeviationsData"],
        "_778": ["ConicalGearManufacturingAnalysis"],
        "_779": ["ConicalGearManufacturingConfig"],
        "_780": ["ConicalGearMicroGeometryConfig"],
        "_781": ["ConicalGearMicroGeometryConfigBase"],
        "_782": ["ConicalMeshedGearManufacturingAnalysis"],
        "_783": ["ConicalMeshedWheelFlankManufacturingConfig"],
        "_784": ["ConicalMeshFlankManufacturingConfig"],
        "_785": ["ConicalMeshFlankMicroGeometryConfig"],
        "_786": ["ConicalMeshFlankNURBSMicroGeometryConfig"],
        "_787": ["ConicalMeshManufacturingAnalysis"],
        "_788": ["ConicalMeshManufacturingConfig"],
        "_789": ["ConicalMeshMicroGeometryConfig"],
        "_790": ["ConicalMeshMicroGeometryConfigBase"],
        "_791": ["ConicalPinionManufacturingConfig"],
        "_792": ["ConicalPinionMicroGeometryConfig"],
        "_793": ["ConicalSetManufacturingAnalysis"],
        "_794": ["ConicalSetManufacturingConfig"],
        "_795": ["ConicalSetMicroGeometryConfig"],
        "_796": ["ConicalSetMicroGeometryConfigBase"],
        "_797": ["ConicalWheelManufacturingConfig"],
        "_798": ["EaseOffBasedTCA"],
        "_799": ["FlankMeasurementBorder"],
        "_800": ["HypoidAdvancedLibrary"],
        "_801": ["MachineTypes"],
        "_802": ["ManufacturingMachine"],
        "_803": ["ManufacturingMachineDatabase"],
        "_804": ["PinionBevelGeneratingModifiedRollMachineSettings"],
        "_805": ["PinionBevelGeneratingTiltMachineSettings"],
        "_806": ["PinionConcave"],
        "_807": ["PinionConicalMachineSettingsSpecified"],
        "_808": ["PinionConvex"],
        "_809": ["PinionFinishMachineSettings"],
        "_810": ["PinionHypoidFormateTiltMachineSettings"],
        "_811": ["PinionHypoidGeneratingTiltMachineSettings"],
        "_812": ["PinionMachineSettingsSMT"],
        "_813": ["PinionRoughMachineSetting"],
        "_814": ["Wheel"],
        "_815": ["WheelFormatMachineTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractTCA",
    "BevelMachineSettingOptimizationResult",
    "ConicalFlankDeviationsData",
    "ConicalGearManufacturingAnalysis",
    "ConicalGearManufacturingConfig",
    "ConicalGearMicroGeometryConfig",
    "ConicalGearMicroGeometryConfigBase",
    "ConicalMeshedGearManufacturingAnalysis",
    "ConicalMeshedWheelFlankManufacturingConfig",
    "ConicalMeshFlankManufacturingConfig",
    "ConicalMeshFlankMicroGeometryConfig",
    "ConicalMeshFlankNURBSMicroGeometryConfig",
    "ConicalMeshManufacturingAnalysis",
    "ConicalMeshManufacturingConfig",
    "ConicalMeshMicroGeometryConfig",
    "ConicalMeshMicroGeometryConfigBase",
    "ConicalPinionManufacturingConfig",
    "ConicalPinionMicroGeometryConfig",
    "ConicalSetManufacturingAnalysis",
    "ConicalSetManufacturingConfig",
    "ConicalSetMicroGeometryConfig",
    "ConicalSetMicroGeometryConfigBase",
    "ConicalWheelManufacturingConfig",
    "EaseOffBasedTCA",
    "FlankMeasurementBorder",
    "HypoidAdvancedLibrary",
    "MachineTypes",
    "ManufacturingMachine",
    "ManufacturingMachineDatabase",
    "PinionBevelGeneratingModifiedRollMachineSettings",
    "PinionBevelGeneratingTiltMachineSettings",
    "PinionConcave",
    "PinionConicalMachineSettingsSpecified",
    "PinionConvex",
    "PinionFinishMachineSettings",
    "PinionHypoidFormateTiltMachineSettings",
    "PinionHypoidGeneratingTiltMachineSettings",
    "PinionMachineSettingsSMT",
    "PinionRoughMachineSetting",
    "Wheel",
    "WheelFormatMachineTypes",
)
