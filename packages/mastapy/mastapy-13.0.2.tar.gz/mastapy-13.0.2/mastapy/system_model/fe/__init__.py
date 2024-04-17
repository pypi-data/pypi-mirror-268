"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2362 import AlignConnectedComponentOptions
    from ._2363 import AlignmentMethod
    from ._2364 import AlignmentMethodForRaceBearing
    from ._2365 import AlignmentUsingAxialNodePositions
    from ._2366 import AngleSource
    from ._2367 import BaseFEWithSelection
    from ._2368 import BatchOperations
    from ._2369 import BearingNodeAlignmentOption
    from ._2370 import BearingNodeOption
    from ._2371 import BearingRaceNodeLink
    from ._2372 import BearingRacePosition
    from ._2373 import ComponentOrientationOption
    from ._2374 import ContactPairWithSelection
    from ._2375 import CoordinateSystemWithSelection
    from ._2376 import CreateConnectedComponentOptions
    from ._2377 import DegreeOfFreedomBoundaryCondition
    from ._2378 import DegreeOfFreedomBoundaryConditionAngular
    from ._2379 import DegreeOfFreedomBoundaryConditionLinear
    from ._2380 import ElectricMachineDataSet
    from ._2381 import ElectricMachineDynamicLoadData
    from ._2382 import ElementFaceGroupWithSelection
    from ._2383 import ElementPropertiesWithSelection
    from ._2384 import FEEntityGroupWithSelection
    from ._2385 import FEExportSettings
    from ._2386 import FEPartDRIVASurfaceSelection
    from ._2387 import FEPartWithBatchOptions
    from ._2388 import FEStiffnessGeometry
    from ._2389 import FEStiffnessTester
    from ._2390 import FESubstructure
    from ._2391 import FESubstructureExportOptions
    from ._2392 import FESubstructureNode
    from ._2393 import FESubstructureNodeModeShape
    from ._2394 import FESubstructureNodeModeShapes
    from ._2395 import FESubstructureType
    from ._2396 import FESubstructureWithBatchOptions
    from ._2397 import FESubstructureWithSelection
    from ._2398 import FESubstructureWithSelectionComponents
    from ._2399 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2400 import FESubstructureWithSelectionForModalAnalysis
    from ._2401 import FESubstructureWithSelectionForStaticAnalysis
    from ._2402 import GearMeshingOptions
    from ._2403 import IndependentMASTACreatedCondensationNode
    from ._2404 import LinkComponentAxialPositionErrorReporter
    from ._2405 import LinkNodeSource
    from ._2406 import MaterialPropertiesWithSelection
    from ._2407 import NodeBoundaryConditionStaticAnalysis
    from ._2408 import NodeGroupWithSelection
    from ._2409 import NodeSelectionDepthOption
    from ._2410 import OptionsWhenExternalFEFileAlreadyExists
    from ._2411 import PerLinkExportOptions
    from ._2412 import PerNodeExportOptions
    from ._2413 import RaceBearingFE
    from ._2414 import RaceBearingFESystemDeflection
    from ._2415 import RaceBearingFEWithSelection
    from ._2416 import ReplacedShaftSelectionHelper
    from ._2417 import SystemDeflectionFEExportOptions
    from ._2418 import ThermalExpansionOption
else:
    import_structure = {
        "_2362": ["AlignConnectedComponentOptions"],
        "_2363": ["AlignmentMethod"],
        "_2364": ["AlignmentMethodForRaceBearing"],
        "_2365": ["AlignmentUsingAxialNodePositions"],
        "_2366": ["AngleSource"],
        "_2367": ["BaseFEWithSelection"],
        "_2368": ["BatchOperations"],
        "_2369": ["BearingNodeAlignmentOption"],
        "_2370": ["BearingNodeOption"],
        "_2371": ["BearingRaceNodeLink"],
        "_2372": ["BearingRacePosition"],
        "_2373": ["ComponentOrientationOption"],
        "_2374": ["ContactPairWithSelection"],
        "_2375": ["CoordinateSystemWithSelection"],
        "_2376": ["CreateConnectedComponentOptions"],
        "_2377": ["DegreeOfFreedomBoundaryCondition"],
        "_2378": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2379": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2380": ["ElectricMachineDataSet"],
        "_2381": ["ElectricMachineDynamicLoadData"],
        "_2382": ["ElementFaceGroupWithSelection"],
        "_2383": ["ElementPropertiesWithSelection"],
        "_2384": ["FEEntityGroupWithSelection"],
        "_2385": ["FEExportSettings"],
        "_2386": ["FEPartDRIVASurfaceSelection"],
        "_2387": ["FEPartWithBatchOptions"],
        "_2388": ["FEStiffnessGeometry"],
        "_2389": ["FEStiffnessTester"],
        "_2390": ["FESubstructure"],
        "_2391": ["FESubstructureExportOptions"],
        "_2392": ["FESubstructureNode"],
        "_2393": ["FESubstructureNodeModeShape"],
        "_2394": ["FESubstructureNodeModeShapes"],
        "_2395": ["FESubstructureType"],
        "_2396": ["FESubstructureWithBatchOptions"],
        "_2397": ["FESubstructureWithSelection"],
        "_2398": ["FESubstructureWithSelectionComponents"],
        "_2399": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2400": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2401": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2402": ["GearMeshingOptions"],
        "_2403": ["IndependentMASTACreatedCondensationNode"],
        "_2404": ["LinkComponentAxialPositionErrorReporter"],
        "_2405": ["LinkNodeSource"],
        "_2406": ["MaterialPropertiesWithSelection"],
        "_2407": ["NodeBoundaryConditionStaticAnalysis"],
        "_2408": ["NodeGroupWithSelection"],
        "_2409": ["NodeSelectionDepthOption"],
        "_2410": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2411": ["PerLinkExportOptions"],
        "_2412": ["PerNodeExportOptions"],
        "_2413": ["RaceBearingFE"],
        "_2414": ["RaceBearingFESystemDeflection"],
        "_2415": ["RaceBearingFEWithSelection"],
        "_2416": ["ReplacedShaftSelectionHelper"],
        "_2417": ["SystemDeflectionFEExportOptions"],
        "_2418": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
