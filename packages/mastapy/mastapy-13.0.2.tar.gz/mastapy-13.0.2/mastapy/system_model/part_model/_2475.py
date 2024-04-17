"""Part"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2210
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.system_model.connections_and_sockets import _2279
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
        _2476,
        _2478,
        _2479,
        _2481,
        _2483,
        _2484,
        _2486,
    )
    from mastapy.system_model.import_export import _2249
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
__all__ = ("Part",)


Self = TypeVar("Self", bound="Part")


class Part(_2210.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE = _PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Part")

    class _Cast_Part:
        """Special nested class for casting Part to subclasses."""

        def __init__(self: "Part._Cast_Part", parent: "Part"):
            self._parent = parent

        @property
        def design_entity(self: "Part._Cast_Part") -> "_2210.DesignEntity":
            return self._parent._cast(_2210.DesignEntity)

        @property
        def assembly(self: "Part._Cast_Part") -> "_2440.Assembly":
            return self._parent._cast(_2440.Assembly)

        @property
        def abstract_assembly(self: "Part._Cast_Part") -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def abstract_shaft(self: "Part._Cast_Part") -> "_2442.AbstractShaft":
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "Part._Cast_Part",
        ) -> "_2443.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.AbstractShaftOrHousing)

        @property
        def bearing(self: "Part._Cast_Part") -> "_2446.Bearing":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Bearing)

        @property
        def bolt(self: "Part._Cast_Part") -> "_2449.Bolt":
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.Bolt)

        @property
        def bolted_joint(self: "Part._Cast_Part") -> "_2450.BoltedJoint":
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.BoltedJoint)

        @property
        def component(self: "Part._Cast_Part") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def connector(self: "Part._Cast_Part") -> "_2454.Connector":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.Connector)

        @property
        def datum(self: "Part._Cast_Part") -> "_2455.Datum":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.Datum)

        @property
        def external_cad_model(self: "Part._Cast_Part") -> "_2459.ExternalCADModel":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.ExternalCADModel)

        @property
        def fe_part(self: "Part._Cast_Part") -> "_2460.FEPart":
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.FEPart)

        @property
        def flexible_pin_assembly(
            self: "Part._Cast_Part",
        ) -> "_2461.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "Part._Cast_Part") -> "_2462.GuideDxfModel":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.GuideDxfModel)

        @property
        def mass_disc(self: "Part._Cast_Part") -> "_2469.MassDisc":
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.MassDisc)

        @property
        def measurement_component(
            self: "Part._Cast_Part",
        ) -> "_2470.MeasurementComponent":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.MeasurementComponent)

        @property
        def mountable_component(self: "Part._Cast_Part") -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def oil_seal(self: "Part._Cast_Part") -> "_2473.OilSeal":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.OilSeal)

        @property
        def planet_carrier(self: "Part._Cast_Part") -> "_2476.PlanetCarrier":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.PlanetCarrier)

        @property
        def point_load(self: "Part._Cast_Part") -> "_2478.PointLoad":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.PointLoad)

        @property
        def power_load(self: "Part._Cast_Part") -> "_2479.PowerLoad":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.PowerLoad)

        @property
        def root_assembly(self: "Part._Cast_Part") -> "_2481.RootAssembly":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.RootAssembly)

        @property
        def specialised_assembly(
            self: "Part._Cast_Part",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "Part._Cast_Part") -> "_2484.UnbalancedMass":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.UnbalancedMass)

        @property
        def virtual_component(self: "Part._Cast_Part") -> "_2486.VirtualComponent":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.VirtualComponent)

        @property
        def shaft(self: "Part._Cast_Part") -> "_2489.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2489

            return self._parent._cast(_2489.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "Part._Cast_Part",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Part._Cast_Part") -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def bevel_gear_set(self: "Part._Cast_Part") -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def concept_gear(self: "Part._Cast_Part") -> "_2528.ConceptGear":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.ConceptGear)

        @property
        def concept_gear_set(self: "Part._Cast_Part") -> "_2529.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.ConceptGearSet)

        @property
        def conical_gear(self: "Part._Cast_Part") -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def conical_gear_set(self: "Part._Cast_Part") -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def cylindrical_gear(self: "Part._Cast_Part") -> "_2532.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "Part._Cast_Part") -> "_2533.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2534.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.CylindricalPlanetGear)

        @property
        def face_gear(self: "Part._Cast_Part") -> "_2535.FaceGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.FaceGear)

        @property
        def face_gear_set(self: "Part._Cast_Part") -> "_2536.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.FaceGearSet)

        @property
        def gear(self: "Part._Cast_Part") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def gear_set(self: "Part._Cast_Part") -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def hypoid_gear(self: "Part._Cast_Part") -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def hypoid_gear_set(self: "Part._Cast_Part") -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "Part._Cast_Part",
        ) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Part._Cast_Part",
        ) -> "_2547.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "Part._Cast_Part") -> "_2549.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "Part._Cast_Part") -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "Part._Cast_Part",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "Part._Cast_Part") -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def worm_gear(self: "Part._Cast_Part") -> "_2558.WormGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.WormGear)

        @property
        def worm_gear_set(self: "Part._Cast_Part") -> "_2559.WormGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.WormGearSet)

        @property
        def zerol_bevel_gear(self: "Part._Cast_Part") -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "Part._Cast_Part") -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "Part._Cast_Part") -> "_2575.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2575

            return self._parent._cast(_2575.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "Part._Cast_Part") -> "_2576.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2576

            return self._parent._cast(_2576.CycloidalDisc)

        @property
        def ring_pins(self: "Part._Cast_Part") -> "_2577.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2577

            return self._parent._cast(_2577.RingPins)

        @property
        def belt_drive(self: "Part._Cast_Part") -> "_2583.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.BeltDrive)

        @property
        def clutch(self: "Part._Cast_Part") -> "_2585.Clutch":
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.Clutch)

        @property
        def clutch_half(self: "Part._Cast_Part") -> "_2586.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.ClutchHalf)

        @property
        def concept_coupling(self: "Part._Cast_Part") -> "_2588.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2589.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.ConceptCouplingHalf)

        @property
        def coupling(self: "Part._Cast_Part") -> "_2591.Coupling":
            from mastapy.system_model.part_model.couplings import _2591

            return self._parent._cast(_2591.Coupling)

        @property
        def coupling_half(self: "Part._Cast_Part") -> "_2592.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.CouplingHalf)

        @property
        def cvt(self: "Part._Cast_Part") -> "_2594.CVT":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.CVT)

        @property
        def cvt_pulley(self: "Part._Cast_Part") -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "Part._Cast_Part",
        ) -> "_2596.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2597.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Part._Cast_Part") -> "_2598.Pulley":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Pulley)

        @property
        def rolling_ring(self: "Part._Cast_Part") -> "_2604.RollingRing":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "Part._Cast_Part",
        ) -> "_2605.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "Part._Cast_Part") -> "_2606.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.ShaftHubConnection)

        @property
        def spring_damper(self: "Part._Cast_Part") -> "_2608.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.SpringDamper)

        @property
        def spring_damper_half(self: "Part._Cast_Part") -> "_2609.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.SpringDamperHalf)

        @property
        def synchroniser(self: "Part._Cast_Part") -> "_2610.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Synchroniser)

        @property
        def synchroniser_half(self: "Part._Cast_Part") -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_part(self: "Part._Cast_Part") -> "_2613.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2613

            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "Part._Cast_Part") -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def torque_converter(self: "Part._Cast_Part") -> "_2615.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2615

            return self._parent._cast(_2615.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "Part._Cast_Part",
        ) -> "_2616.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "Part._Cast_Part",
        ) -> "_2618.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.TorqueConverterTurbine)

        @property
        def part(self: "Part._Cast_Part") -> "Part":
            return self._parent

        def __getattr__(self: "Part._Cast_Part", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Part.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_full_model(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingFullModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_isometric_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def drawing_number(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DrawingNumber

        if temp is None:
            return ""

        return temp

    @drawing_number.setter
    @enforce_parameter_types
    def drawing_number(self: Self, value: "str"):
        self.wrapped.DrawingNumber = str(value) if value is not None else ""

    @property
    def editable_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditableName

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: Self, value: "str"):
        self.wrapped.EditableName = str(value) if value is not None else ""

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

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
    def mass_properties_from_design(self: Self) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_design_including_planetary_duplicates(
        self: Self,
    ) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesignIncludingPlanetaryDuplicates

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connections(self: Self) -> "List[_2279.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def local_connections(self: Self) -> "List[_2279.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def connections_to(self: Self, part: "Part") -> "List[_2279.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Args:
            part (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ConnectionsTo(part.wrapped if part else None)
        )

    @enforce_parameter_types
    def copy_to(self: Self, container: "_2440.Assembly") -> "Part":
        """mastapy.system_model.part_model.Part

        Args:
            container (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.CopyTo(container.wrapped if container else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_geometry_export_options(self: Self) -> "_2249.GeometryExportOptions":
        """mastapy.system_model.import_export.GeometryExportOptions"""
        method_result = self.wrapped.CreateGeometryExportOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_connections(self: Self):
        """Method does not return."""
        self.wrapped.DeleteConnections()

    @property
    def cast_to(self: Self) -> "Part._Cast_Part":
        return self._Cast_Part(self)
