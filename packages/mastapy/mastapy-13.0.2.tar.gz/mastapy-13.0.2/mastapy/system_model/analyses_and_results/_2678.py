"""CompoundHarmonicAnalysisOfSingleExcitationAnalysis"""

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
_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
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
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6250,
        _6265,
        _6148,
        _6147,
        _6149,
        _6155,
        _6166,
        _6167,
        _6172,
        _6183,
        _6198,
        _6199,
        _6203,
        _6204,
        _6154,
        _6208,
        _6222,
        _6223,
        _6224,
        _6225,
        _6226,
        _6232,
        _6233,
        _6234,
        _6241,
        _6245,
        _6268,
        _6269,
        _6242,
        _6176,
        _6178,
        _6200,
        _6202,
        _6151,
        _6153,
        _6158,
        _6160,
        _6161,
        _6162,
        _6163,
        _6165,
        _6179,
        _6181,
        _6194,
        _6196,
        _6197,
        _6205,
        _6207,
        _6209,
        _6211,
        _6213,
        _6215,
        _6216,
        _6218,
        _6219,
        _6221,
        _6231,
        _6246,
        _6248,
        _6252,
        _6254,
        _6255,
        _6257,
        _6258,
        _6259,
        _6270,
        _6272,
        _6273,
        _6275,
        _6190,
        _6192,
        _6236,
        _6227,
        _6229,
        _6157,
        _6168,
        _6170,
        _6173,
        _6175,
        _6184,
        _6186,
        _6188,
        _6189,
        _6235,
        _6243,
        _6239,
        _6238,
        _6249,
        _6251,
        _6260,
        _6261,
        _6262,
        _6263,
        _6264,
        _6266,
        _6267,
        _6244,
        _6187,
        _6156,
        _6171,
        _6182,
        _6212,
        _6230,
        _6240,
        _6150,
        _6159,
        _6177,
        _6201,
        _6253,
        _6164,
        _6180,
        _6152,
        _6195,
        _6210,
        _6214,
        _6217,
        _6220,
        _6247,
        _6256,
        _6271,
        _6274,
        _6206,
        _6191,
        _6193,
        _6237,
        _6228,
        _6169,
        _6174,
        _6185,
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
__all__ = ("CompoundHarmonicAnalysisOfSingleExcitationAnalysis",)


Self = TypeVar("Self", bound="CompoundHarmonicAnalysisOfSingleExcitationAnalysis")


class CompoundHarmonicAnalysisOfSingleExcitationAnalysis(_2627.CompoundAnalysis):
    """CompoundHarmonicAnalysisOfSingleExcitationAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis"
    )

    class _Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis:
        """Special nested class for casting CompoundHarmonicAnalysisOfSingleExcitationAnalysis to subclasses."""

        def __init__(
            self: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
            parent: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_harmonic_analysis_of_single_excitation_analysis(
            self: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
        ) -> "CompoundHarmonicAnalysisOfSingleExcitationAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "CompoundHarmonicAnalysisOfSingleExcitationAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2357.SpringDamperConnection"
    ) -> "Iterable[_6250.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6265.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6148.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6149.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6155.BearingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BearingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6166.BoltCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BoltCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6167.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ComponentCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6183.ConnectorCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConnectorCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6198.DatumCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.DatumCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6199.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6203.FEPartCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FEPartCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6204.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6208.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MassDiscCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6225.OilSealCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.OilSealCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6226.PartCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6232.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PointLoadCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6241.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6245.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6242.ShaftCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6176.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6178.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6200.FaceGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6202.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6151.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6153.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6158.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6160.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6161.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6162.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6163.BevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6165.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6179.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6181.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6194.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6196.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6197.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6205.GearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6207.GearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6209.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6211.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6213.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6215.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6216.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6218.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6219.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6221.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6231.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6246.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6248.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6252.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6254.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6255.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6257.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6258.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6259.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6270.WormGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6272.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6273.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6275.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6190.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6192.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6236.RingPinsCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RingPinsCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6227.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6229.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6157.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6168.ClutchCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6170.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6173.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6175.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6184.CouplingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6186.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6188.CVTCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6189.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6235.PulleyCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PulleyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6243.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6239.RollingRingCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6238.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6249.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6251.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6260.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6261.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6262.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6263.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6264.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6266.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6267.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6244.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6187.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6156.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6171.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6230.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6240.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6159.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6177.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6201.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6253.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6164.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6180.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6152.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6195.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6210.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6214.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6217.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6220.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> (
        "Iterable[_6247.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6256.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6271.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6274.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6206.GearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearMeshCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6191.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6193.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6237.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6228.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6169.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6174.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "Iterable[_6185.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundHarmonicAnalysisOfSingleExcitationAnalysis._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis":
        return self._Cast_CompoundHarmonicAnalysisOfSingleExcitationAnalysis(self)
