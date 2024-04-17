"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2440 import Assembly
    from ._2441 import AbstractAssembly
    from ._2442 import AbstractShaft
    from ._2443 import AbstractShaftOrHousing
    from ._2444 import AGMALoadSharingTableApplicationLevel
    from ._2445 import AxialInternalClearanceTolerance
    from ._2446 import Bearing
    from ._2447 import BearingF0InputMethod
    from ._2448 import BearingRaceMountingOptions
    from ._2449 import Bolt
    from ._2450 import BoltedJoint
    from ._2451 import Component
    from ._2452 import ComponentsConnectedResult
    from ._2453 import ConnectedSockets
    from ._2454 import Connector
    from ._2455 import Datum
    from ._2456 import ElectricMachineSearchRegionSpecificationMethod
    from ._2457 import EnginePartLoad
    from ._2458 import EngineSpeed
    from ._2459 import ExternalCADModel
    from ._2460 import FEPart
    from ._2461 import FlexiblePinAssembly
    from ._2462 import GuideDxfModel
    from ._2463 import GuideImage
    from ._2464 import GuideModelUsage
    from ._2465 import InnerBearingRaceMountingOptions
    from ._2466 import InternalClearanceTolerance
    from ._2467 import LoadSharingModes
    from ._2468 import LoadSharingSettings
    from ._2469 import MassDisc
    from ._2470 import MeasurementComponent
    from ._2471 import MountableComponent
    from ._2472 import OilLevelSpecification
    from ._2473 import OilSeal
    from ._2474 import OuterBearingRaceMountingOptions
    from ._2475 import Part
    from ._2476 import PlanetCarrier
    from ._2477 import PlanetCarrierSettings
    from ._2478 import PointLoad
    from ._2479 import PowerLoad
    from ._2480 import RadialInternalClearanceTolerance
    from ._2481 import RootAssembly
    from ._2482 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2483 import SpecialisedAssembly
    from ._2484 import UnbalancedMass
    from ._2485 import UnbalancedMassInclusionOption
    from ._2486 import VirtualComponent
    from ._2487 import WindTurbineBladeModeDetails
    from ._2488 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        "_2440": ["Assembly"],
        "_2441": ["AbstractAssembly"],
        "_2442": ["AbstractShaft"],
        "_2443": ["AbstractShaftOrHousing"],
        "_2444": ["AGMALoadSharingTableApplicationLevel"],
        "_2445": ["AxialInternalClearanceTolerance"],
        "_2446": ["Bearing"],
        "_2447": ["BearingF0InputMethod"],
        "_2448": ["BearingRaceMountingOptions"],
        "_2449": ["Bolt"],
        "_2450": ["BoltedJoint"],
        "_2451": ["Component"],
        "_2452": ["ComponentsConnectedResult"],
        "_2453": ["ConnectedSockets"],
        "_2454": ["Connector"],
        "_2455": ["Datum"],
        "_2456": ["ElectricMachineSearchRegionSpecificationMethod"],
        "_2457": ["EnginePartLoad"],
        "_2458": ["EngineSpeed"],
        "_2459": ["ExternalCADModel"],
        "_2460": ["FEPart"],
        "_2461": ["FlexiblePinAssembly"],
        "_2462": ["GuideDxfModel"],
        "_2463": ["GuideImage"],
        "_2464": ["GuideModelUsage"],
        "_2465": ["InnerBearingRaceMountingOptions"],
        "_2466": ["InternalClearanceTolerance"],
        "_2467": ["LoadSharingModes"],
        "_2468": ["LoadSharingSettings"],
        "_2469": ["MassDisc"],
        "_2470": ["MeasurementComponent"],
        "_2471": ["MountableComponent"],
        "_2472": ["OilLevelSpecification"],
        "_2473": ["OilSeal"],
        "_2474": ["OuterBearingRaceMountingOptions"],
        "_2475": ["Part"],
        "_2476": ["PlanetCarrier"],
        "_2477": ["PlanetCarrierSettings"],
        "_2478": ["PointLoad"],
        "_2479": ["PowerLoad"],
        "_2480": ["RadialInternalClearanceTolerance"],
        "_2481": ["RootAssembly"],
        "_2482": ["ShaftDiameterModificationDueToRollingBearingRing"],
        "_2483": ["SpecialisedAssembly"],
        "_2484": ["UnbalancedMass"],
        "_2485": ["UnbalancedMassInclusionOption"],
        "_2486": ["VirtualComponent"],
        "_2487": ["WindTurbineBladeModeDetails"],
        "_2488": ["WindTurbineSingleBladeDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
