"""DesignEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2207
    from mastapy.utility.model_validation import _1801, _1800
    from mastapy.utility.scripting import _1748
    from mastapy.system_model.connections_and_sockets import (
        _2272,
        _2275,
        _2276,
        _2279,
        _2280,
        _2288,
        _2294,
        _2299,
        _2302,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2306,
        _2308,
        _2310,
        _2312,
        _2314,
        _2316,
        _2318,
        _2320,
        _2322,
        _2325,
        _2326,
        _2327,
        _2330,
        _2332,
        _2334,
        _2336,
        _2338,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2342,
        _2345,
        _2348,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2349,
        _2351,
        _2353,
        _2355,
        _2357,
        _2359,
    )
    from mastapy.system_model.part_model import (
        _2440,
        _2441,
        _2442,
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
        _2520,
        _2521,
        _2522,
        _2523,
        _2524,
        _2525,
        _2526,
        _2527,
        _2528,
        _2529,
        _2530,
        _2531,
        _2532,
        _2533,
        _2534,
        _2535,
        _2536,
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
        _2583,
        _2585,
        _2586,
        _2588,
        _2589,
        _2591,
        _2592,
        _2594,
        _2595,
        _2596,
        _2597,
        _2598,
        _2604,
        _2605,
        _2606,
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


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2272.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2275.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2275

            return self._parent._cast(_2275.BeltConnection)

        @property
        def coaxial_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2276.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity") -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def cvt_belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2280.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2294.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2299.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2302.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2302

            return self._parent._cast(_2302.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2310.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2312.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2314.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2316.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2318.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity") -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2322.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2336.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2342.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2342

            return self._parent._cast(_2342.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2345

            return self._parent._cast(_2345.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2348.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2348

            return self._parent._cast(_2348.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2349.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2351.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2353.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2355.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2355

            return self._parent._cast(_2355.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2357.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2357

            return self._parent._cast(_2357.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2359.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2359

            return self._parent._cast(_2359.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity") -> "_2440.Assembly":
            from mastapy.system_model.part_model import _2440

            return self._parent._cast(_2440.Assembly)

        @property
        def abstract_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def abstract_shaft(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2442.AbstractShaft":
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2443.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity") -> "_2446.Bearing":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity") -> "_2449.Bolt":
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.Bolt)

        @property
        def bolted_joint(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2450.BoltedJoint":
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity") -> "_2454.Connector":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity") -> "_2455.Datum":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.Datum)

        @property
        def external_cad_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2459.ExternalCADModel":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity") -> "_2460.FEPart":
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.FEPart)

        @property
        def flexible_pin_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2461.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.FlexiblePinAssembly)

        @property
        def guide_dxf_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2462.GuideDxfModel":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity") -> "_2469.MassDisc":
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.MassDisc)

        @property
        def measurement_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2470.MeasurementComponent":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.MeasurementComponent)

        @property
        def mountable_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity") -> "_2473.OilSeal":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def planet_carrier(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2476.PlanetCarrier":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity") -> "_2478.PointLoad":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity") -> "_2479.PowerLoad":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.PowerLoad)

        @property
        def root_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2481.RootAssembly":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.RootAssembly)

        @property
        def specialised_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def unbalanced_mass(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2484.UnbalancedMass":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.UnbalancedMass)

        @property
        def virtual_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2486.VirtualComponent":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity") -> "_2489.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2489

            return self._parent._cast(_2489.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def concept_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2528.ConceptGear":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.ConceptGear)

        @property
        def concept_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2529.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.ConceptGearSet)

        @property
        def conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def cylindrical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2532.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.CylindricalGear)

        @property
        def cylindrical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2533.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2534.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2535.FaceGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.FaceGear)

        @property
        def face_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2536.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity") -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2547.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2549.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2558.WormGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.WormGear)

        @property
        def worm_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2559.WormGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.WormGearSet)

        @property
        def zerol_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2575.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2575

            return self._parent._cast(_2575.CycloidalAssembly)

        @property
        def cycloidal_disc(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2576.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2576

            return self._parent._cast(_2576.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity") -> "_2577.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2577

            return self._parent._cast(_2577.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity") -> "_2583.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity") -> "_2585.Clutch":
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity") -> "_2586.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.ClutchHalf)

        @property
        def concept_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2588.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2589.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity") -> "_2591.Coupling":
            from mastapy.system_model.part_model.couplings import _2591

            return self._parent._cast(_2591.Coupling)

        @property
        def coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2592.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity") -> "_2594.CVT":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2596.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2597.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2598.Pulley":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Pulley)

        @property
        def rolling_ring(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2604.RollingRing":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2605.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.RollingRingAssembly)

        @property
        def shaft_hub_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2606.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.ShaftHubConnection)

        @property
        def spring_damper(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2608.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.SpringDamper)

        @property
        def spring_damper_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2609.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.SpringDamperHalf)

        @property
        def synchroniser(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2610.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Synchroniser)

        @property
        def synchroniser_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2613.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2613

            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def torque_converter(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2615.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2615

            return self._parent._cast(_2615.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2616.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2618.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def design_properties(self: Self) -> "_2207.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1801.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1800.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1748.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)
