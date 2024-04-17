"""CompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException

_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2357,
        _2359,
        _2355,
        _2349,
        _2351,
        _2353,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4839,
        _4854,
        _4737,
        _4736,
        _4738,
        _4744,
        _4755,
        _4756,
        _4761,
        _4772,
        _4787,
        _4788,
        _4792,
        _4793,
        _4743,
        _4797,
        _4811,
        _4812,
        _4813,
        _4814,
        _4815,
        _4821,
        _4822,
        _4823,
        _4830,
        _4834,
        _4857,
        _4858,
        _4831,
        _4765,
        _4767,
        _4789,
        _4791,
        _4740,
        _4742,
        _4747,
        _4749,
        _4750,
        _4751,
        _4752,
        _4754,
        _4768,
        _4770,
        _4783,
        _4785,
        _4786,
        _4794,
        _4796,
        _4798,
        _4800,
        _4802,
        _4804,
        _4805,
        _4807,
        _4808,
        _4810,
        _4820,
        _4835,
        _4837,
        _4841,
        _4843,
        _4844,
        _4846,
        _4847,
        _4848,
        _4859,
        _4861,
        _4862,
        _4864,
        _4779,
        _4781,
        _4825,
        _4816,
        _4818,
        _4746,
        _4757,
        _4759,
        _4762,
        _4764,
        _4773,
        _4775,
        _4777,
        _4778,
        _4824,
        _4832,
        _4828,
        _4827,
        _4838,
        _4840,
        _4849,
        _4850,
        _4851,
        _4852,
        _4853,
        _4855,
        _4856,
        _4833,
        _4776,
        _4745,
        _4760,
        _4771,
        _4801,
        _4819,
        _4829,
        _4739,
        _4748,
        _4766,
        _4790,
        _4842,
        _4753,
        _4769,
        _4741,
        _4784,
        _4799,
        _4803,
        _4806,
        _4809,
        _4836,
        _4845,
        _4860,
        _4863,
        _4795,
        _4780,
        _4782,
        _4826,
        _4817,
        _4758,
        _4763,
        _4774,
    )
    from mastapy.system_model.part_model import (
        _2442,
        _2441,
        _2443,
        _2446,
        _2449,
        _2450,
        _2451,
        _2454,
        _2455,
        _2459,
        _2460,
        _2461,
        _2440,
        _2462,
        _2469,
        _2470,
        _2471,
        _2473,
        _2475,
        _2476,
        _2478,
        _2479,
        _2481,
        _2483,
        _2484,
        _2486,
    )
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.part_model.gears import (
        _2528,
        _2529,
        _2535,
        _2536,
        _2520,
        _2521,
        _2522,
        _2523,
        _2524,
        _2525,
        _2526,
        _2527,
        _2530,
        _2531,
        _2532,
        _2533,
        _2534,
        _2537,
        _2539,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
        _2552,
        _2553,
        _2554,
        _2555,
        _2556,
        _2557,
        _2558,
        _2559,
        _2560,
        _2561,
    )
    from mastapy.system_model.part_model.cycloidal import _2575, _2576, _2577
    from mastapy.system_model.part_model.couplings import (
        _2596,
        _2597,
        _2583,
        _2585,
        _2586,
        _2588,
        _2589,
        _2591,
        _2592,
        _2594,
        _2595,
        _2598,
        _2606,
        _2604,
        _2605,
        _2608,
        _2609,
        _2610,
        _2612,
        _2613,
        _2614,
        _2615,
        _2616,
        _2618,
    )
    from mastapy.system_model.connections_and_sockets import (
        _2302,
        _2280,
        _2275,
        _2276,
        _2279,
        _2288,
        _2294,
        _2299,
        _2272,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2308,
        _2312,
        _2318,
        _2332,
        _2310,
        _2314,
        _2306,
        _2316,
        _2322,
        _2325,
        _2326,
        _2327,
        _2330,
        _2334,
        _2336,
        _2338,
        _2320,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2342,
        _2345,
        _2348,
    )
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundModalAnalysis",)


Self = TypeVar("Self", bound="CompoundModalAnalysis")


class CompoundModalAnalysis(_2627.CompoundAnalysis):
    """CompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundModalAnalysis")

    class _Cast_CompoundModalAnalysis:
        """Special nested class for casting CompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CompoundModalAnalysis._Cast_CompoundModalAnalysis",
            parent: "CompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundModalAnalysis._Cast_CompoundModalAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundModalAnalysis._Cast_CompoundModalAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_modal_analysis(
            self: "CompoundModalAnalysis._Cast_CompoundModalAnalysis",
        ) -> "CompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundModalAnalysis._Cast_CompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2357.SpringDamperConnection"
    ) -> "Iterable[_4839.SpringDamperConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: Self, design_entity: "_2359.TorqueConverterConnection"
    ) -> "Iterable[_4854.TorqueConverterConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: Self, design_entity: "_2442.AbstractShaft"
    ) -> "Iterable[_4737.AbstractShaftCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: Self, design_entity: "_2441.AbstractAssembly"
    ) -> "Iterable[_4736.AbstractAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2443.AbstractShaftOrHousing"
    ) -> "Iterable[_4738.AbstractShaftOrHousingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftOrHousingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: Self, design_entity: "_2446.Bearing"
    ) -> "Iterable[_4744.BearingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BearingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEARING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: Self, design_entity: "_2449.Bolt"
    ) -> "Iterable[_4755.BoltCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BoltCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: Self, design_entity: "_2450.BoltedJoint"
    ) -> "Iterable[_4756.BoltedJointCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BoltedJointCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_component(
        self: Self, design_entity: "_2451.Component"
    ) -> "Iterable[_4761.ComponentCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ComponentCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connector(
        self: Self, design_entity: "_2454.Connector"
    ) -> "Iterable[_4772.ConnectorCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConnectorCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTOR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_datum(
        self: Self, design_entity: "_2455.Datum"
    ) -> "Iterable[_4787.DatumCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.DatumCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_DATUM](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: Self, design_entity: "_2459.ExternalCADModel"
    ) -> "Iterable[_4788.ExternalCADModelCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ExternalCADModelCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: Self, design_entity: "_2460.FEPart"
    ) -> "Iterable[_4792.FEPartCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FEPartCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FE_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: Self, design_entity: "_2461.FlexiblePinAssembly"
    ) -> "Iterable[_4793.FlexiblePinAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FlexiblePinAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: Self, design_entity: "_2440.Assembly"
    ) -> "Iterable[_4743.AssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: Self, design_entity: "_2462.GuideDxfModel"
    ) -> "Iterable[_4797.GuideDxfModelCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GuideDxfModelCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: Self, design_entity: "_2469.MassDisc"
    ) -> "Iterable[_4811.MassDiscCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MassDiscCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MASS_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: Self, design_entity: "_2470.MeasurementComponent"
    ) -> "Iterable[_4812.MeasurementComponentCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MeasurementComponentCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: Self, design_entity: "_2471.MountableComponent"
    ) -> "Iterable[_4813.MountableComponentCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MountableComponentCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: Self, design_entity: "_2473.OilSeal"
    ) -> "Iterable[_4814.OilSealCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.OilSealCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part(
        self: Self, design_entity: "_2475.Part"
    ) -> "Iterable[_4815.PartCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: Self, design_entity: "_2476.PlanetCarrier"
    ) -> "Iterable[_4821.PlanetCarrierCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetCarrierCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: Self, design_entity: "_2478.PointLoad"
    ) -> "Iterable[_4822.PointLoadCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PointLoadCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: Self, design_entity: "_2479.PowerLoad"
    ) -> "Iterable[_4823.PowerLoadCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PowerLoadCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: Self, design_entity: "_2481.RootAssembly"
    ) -> "Iterable[_4830.RootAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RootAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: Self, design_entity: "_2483.SpecialisedAssembly"
    ) -> "Iterable[_4834.SpecialisedAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpecialisedAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: Self, design_entity: "_2484.UnbalancedMass"
    ) -> "Iterable[_4857.UnbalancedMassCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.UnbalancedMassCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: Self, design_entity: "_2486.VirtualComponent"
    ) -> "Iterable[_4858.VirtualComponentCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.VirtualComponentCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: Self, design_entity: "_2489.Shaft"
    ) -> "Iterable[_4831.ShaftCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: Self, design_entity: "_2528.ConceptGear"
    ) -> "Iterable[_4765.ConceptGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: Self, design_entity: "_2529.ConceptGearSet"
    ) -> "Iterable[_4767.ConceptGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: Self, design_entity: "_2535.FaceGear"
    ) -> "Iterable[_4789.FaceGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: Self, design_entity: "_2536.FaceGearSet"
    ) -> "Iterable[_4791.FaceGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2520.AGMAGleasonConicalGear"
    ) -> "Iterable[_4740.AGMAGleasonConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2521.AGMAGleasonConicalGearSet"
    ) -> "Iterable[_4742.AGMAGleasonConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: Self, design_entity: "_2522.BevelDifferentialGear"
    ) -> "Iterable[_4747.BevelDifferentialGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2523.BevelDifferentialGearSet"
    ) -> "Iterable[_4749.BevelDifferentialGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2524.BevelDifferentialPlanetGear"
    ) -> "Iterable[_4750.BevelDifferentialPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialPlanetGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2525.BevelDifferentialSunGear"
    ) -> "Iterable[_4751.BevelDifferentialSunGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialSunGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: Self, design_entity: "_2526.BevelGear"
    ) -> "Iterable[_4752.BevelGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: Self, design_entity: "_2527.BevelGearSet"
    ) -> "Iterable[_4754.BevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: Self, design_entity: "_2530.ConicalGear"
    ) -> "Iterable[_4768.ConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: Self, design_entity: "_2531.ConicalGearSet"
    ) -> "Iterable[_4770.ConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: Self, design_entity: "_2532.CylindricalGear"
    ) -> "Iterable[_4783.CylindricalGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: Self, design_entity: "_2533.CylindricalGearSet"
    ) -> "Iterable[_4785.CylindricalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2534.CylindricalPlanetGear"
    ) -> "Iterable[_4786.CylindricalPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalPlanetGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear(
        self: Self, design_entity: "_2537.Gear"
    ) -> "Iterable[_4794.GearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: Self, design_entity: "_2539.GearSet"
    ) -> "Iterable[_4796.GearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: Self, design_entity: "_2541.HypoidGear"
    ) -> "Iterable[_4798.HypoidGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: Self, design_entity: "_2542.HypoidGearSet"
    ) -> "Iterable[_4800.HypoidGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2543.KlingelnbergCycloPalloidConicalGear"
    ) -> "Iterable[_4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2544.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "Iterable[_4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2545.KlingelnbergCycloPalloidHypoidGear"
    ) -> "Iterable[_4805.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2546.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "Iterable[_4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2547.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "Iterable[_4808.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "Iterable[_4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: Self, design_entity: "_2549.PlanetaryGearSet"
    ) -> "Iterable[_4820.PlanetaryGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetaryGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: Self, design_entity: "_2550.SpiralBevelGear"
    ) -> "Iterable[_4835.SpiralBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2551.SpiralBevelGearSet"
    ) -> "Iterable[_4837.SpiralBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2552.StraightBevelDiffGear"
    ) -> "Iterable[_4841.StraightBevelDiffGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2553.StraightBevelDiffGearSet"
    ) -> "Iterable[_4843.StraightBevelDiffGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: Self, design_entity: "_2554.StraightBevelGear"
    ) -> "Iterable[_4844.StraightBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2555.StraightBevelGearSet"
    ) -> "Iterable[_4846.StraightBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2556.StraightBevelPlanetGear"
    ) -> "Iterable[_4847.StraightBevelPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelPlanetGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2557.StraightBevelSunGear"
    ) -> "Iterable[_4848.StraightBevelSunGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelSunGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: Self, design_entity: "_2558.WormGear"
    ) -> "Iterable[_4859.WormGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: Self, design_entity: "_2559.WormGearSet"
    ) -> "Iterable[_4861.WormGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: Self, design_entity: "_2560.ZerolBevelGear"
    ) -> "Iterable[_4862.ZerolBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2561.ZerolBevelGearSet"
    ) -> "Iterable[_4864.ZerolBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearSetCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: Self, design_entity: "_2575.CycloidalAssembly"
    ) -> "Iterable[_4779.CycloidalAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CycloidalAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: Self, design_entity: "_2576.CycloidalDisc"
    ) -> "Iterable[_4781.CycloidalDiscCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: Self, design_entity: "_2577.RingPins"
    ) -> "Iterable[_4825.RingPinsCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RingPinsCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2596.PartToPartShearCoupling"
    ) -> "Iterable[_4816.PartToPartShearCouplingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2597.PartToPartShearCouplingHalf"
    ) -> "Iterable[_4818.PartToPartShearCouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: Self, design_entity: "_2583.BeltDrive"
    ) -> "Iterable[_4746.BeltDriveCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BeltDriveCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: Self, design_entity: "_2585.Clutch"
    ) -> "Iterable[_4757.ClutchCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: Self, design_entity: "_2586.ClutchHalf"
    ) -> "Iterable[_4759.ClutchHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: Self, design_entity: "_2588.ConceptCoupling"
    ) -> "Iterable[_4762.ConceptCouplingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: Self, design_entity: "_2589.ConceptCouplingHalf"
    ) -> "Iterable[_4764.ConceptCouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: Self, design_entity: "_2591.Coupling"
    ) -> "Iterable[_4773.CouplingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: Self, design_entity: "_2592.CouplingHalf"
    ) -> "Iterable[_4775.CouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: Self, design_entity: "_2594.CVT"
    ) -> "Iterable[_4777.CVTCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: Self, design_entity: "_2595.CVTPulley"
    ) -> "Iterable[_4778.CVTPulleyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTPulleyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: Self, design_entity: "_2598.Pulley"
    ) -> "Iterable[_4824.PulleyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PulleyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: Self, design_entity: "_2606.ShaftHubConnection"
    ) -> "Iterable[_4832.ShaftHubConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftHubConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: Self, design_entity: "_2604.RollingRing"
    ) -> "Iterable[_4828.RollingRingCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: Self, design_entity: "_2605.RollingRingAssembly"
    ) -> "Iterable[_4827.RollingRingAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingAssemblyCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: Self, design_entity: "_2608.SpringDamper"
    ) -> "Iterable[_4838.SpringDamperCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: Self, design_entity: "_2609.SpringDamperHalf"
    ) -> "Iterable[_4840.SpringDamperHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: Self, design_entity: "_2610.Synchroniser"
    ) -> "Iterable[_4849.SynchroniserCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: Self, design_entity: "_2612.SynchroniserHalf"
    ) -> "Iterable[_4850.SynchroniserHalfCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserHalfCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: Self, design_entity: "_2613.SynchroniserPart"
    ) -> "Iterable[_4851.SynchroniserPartCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserPartCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: Self, design_entity: "_2614.SynchroniserSleeve"
    ) -> "Iterable[_4852.SynchroniserSleeveCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserSleeveCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: Self, design_entity: "_2615.TorqueConverter"
    ) -> "Iterable[_4853.TorqueConverterCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: Self, design_entity: "_2616.TorqueConverterPump"
    ) -> "Iterable[_4855.TorqueConverterPumpCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterPumpCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: Self, design_entity: "_2618.TorqueConverterTurbine"
    ) -> "Iterable[_4856.TorqueConverterTurbineCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterTurbineCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2302.ShaftToMountableComponentConnection"
    ) -> "Iterable[_4833.ShaftToMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftToMountableComponentConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: Self, design_entity: "_2280.CVTBeltConnection"
    ) -> "Iterable[_4776.CVTBeltConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTBeltConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: Self, design_entity: "_2275.BeltConnection"
    ) -> "Iterable[_4745.BeltConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BeltConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: Self, design_entity: "_2276.CoaxialConnection"
    ) -> "Iterable[_4760.CoaxialConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CoaxialConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connection(
        self: Self, design_entity: "_2279.Connection"
    ) -> "Iterable[_4771.ConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2288.InterMountableComponentConnection"
    ) -> "Iterable[_4801.InterMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.InterMountableComponentConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: Self, design_entity: "_2294.PlanetaryConnection"
    ) -> "Iterable[_4819.PlanetaryConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetaryConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: Self, design_entity: "_2299.RollingRingConnection"
    ) -> "Iterable[_4829.RollingRingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2272.AbstractShaftToMountableComponentConnection"
    ) -> "Iterable[_4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2308.BevelDifferentialGearMesh"
    ) -> "Iterable[_4748.BevelDifferentialGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: Self, design_entity: "_2312.ConceptGearMesh"
    ) -> "Iterable[_4766.ConceptGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: Self, design_entity: "_2318.FaceGearMesh"
    ) -> "Iterable[_4790.FaceGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2332.StraightBevelDiffGearMesh"
    ) -> "Iterable[_4842.StraightBevelDiffGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: Self, design_entity: "_2310.BevelGearMesh"
    ) -> "Iterable[_4753.BevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: Self, design_entity: "_2314.ConicalGearMesh"
    ) -> "Iterable[_4769.ConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2306.AGMAGleasonConicalGearMesh"
    ) -> "Iterable[_4741.AGMAGleasonConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2316.CylindricalGearMesh"
    ) -> "Iterable[_4784.CylindricalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2322.HypoidGearMesh"
    ) -> "Iterable[_4799.HypoidGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2325.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "Iterable[_4803.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2326.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "Iterable[_4806.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "Iterable[_4809.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2330.SpiralBevelGearMesh"
    ) -> "Iterable[_4836.SpiralBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2334.StraightBevelGearMesh"
    ) -> "Iterable[_4845.StraightBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: Self, design_entity: "_2336.WormGearMesh"
    ) -> "Iterable[_4860.WormGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2338.ZerolBevelGearMesh"
    ) -> "Iterable[_4863.ZerolBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: Self, design_entity: "_2320.GearMesh"
    ) -> "Iterable[_4795.GearMeshCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearMeshCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2342.CycloidalDiscCentralBearingConnection"
    ) -> "Iterable[_4780.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2345.CycloidalDiscPlanetaryBearingConnection"
    ) -> "Iterable[_4782.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2348.RingPinsToDiscConnection"
    ) -> "Iterable[_4826.RingPinsToDiscConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RingPinsToDiscConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2355.PartToPartShearCouplingConnection"
    ) -> "Iterable[_4817.PartToPartShearCouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: Self, design_entity: "_2349.ClutchConnection"
    ) -> "Iterable[_4758.ClutchConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: Self, design_entity: "_2351.ConceptCouplingConnection"
    ) -> "Iterable[_4763.ConceptCouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: Self, design_entity: "_2353.CouplingConnection"
    ) -> "Iterable[_4774.CouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(self: Self) -> "CompoundModalAnalysis._Cast_CompoundModalAnalysis":
        return self._Cast_CompoundModalAnalysis(self)
