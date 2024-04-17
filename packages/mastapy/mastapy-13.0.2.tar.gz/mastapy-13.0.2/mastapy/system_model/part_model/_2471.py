"""MountableComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2442,
        _2452,
        _2446,
        _2454,
        _2469,
        _2470,
        _2473,
        _2476,
        _2478,
        _2479,
        _2484,
        _2486,
        _2475,
    )
    from mastapy.system_model.connections_and_sockets import _2279, _2283, _2276
    from mastapy.system_model.part_model.gears import (
        _2520,
        _2522,
        _2524,
        _2525,
        _2526,
        _2528,
        _2530,
        _2532,
        _2534,
        _2535,
        _2537,
        _2541,
        _2543,
        _2545,
        _2547,
        _2550,
        _2552,
        _2554,
        _2556,
        _2557,
        _2558,
        _2560,
    )
    from mastapy.system_model.part_model.cycloidal import _2577
    from mastapy.system_model.part_model.couplings import (
        _2586,
        _2589,
        _2592,
        _2595,
        _2597,
        _2598,
        _2604,
        _2606,
        _2609,
        _2612,
        _2613,
        _2614,
        _2616,
        _2618,
    )
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2451.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bearing(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2446.Bearing":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Bearing)

        @property
        def connector(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2454.Connector":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.Connector)

        @property
        def mass_disc(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2469.MassDisc":
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.MassDisc)

        @property
        def measurement_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2470.MeasurementComponent":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.MeasurementComponent)

        @property
        def oil_seal(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2473.OilSeal":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.OilSeal)

        @property
        def planet_carrier(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2476.PlanetCarrier":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.PlanetCarrier)

        @property
        def point_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2478.PointLoad":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.PointLoad)

        @property
        def power_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2479.PowerLoad":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.PowerLoad)

        @property
        def unbalanced_mass(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2484.UnbalancedMass":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.UnbalancedMass)

        @property
        def virtual_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2486.VirtualComponent":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def concept_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2528.ConceptGear":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.ConceptGear)

        @property
        def conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def cylindrical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2532.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2534.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.CylindricalPlanetGear)

        @property
        def face_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2535.FaceGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2547.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def worm_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2558.WormGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.WormGear)

        @property
        def zerol_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def ring_pins(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2577.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2577

            return self._parent._cast(_2577.RingPins)

        @property
        def clutch_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2586.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2589.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.ConceptCouplingHalf)

        @property
        def coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2592.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.CouplingHalf)

        @property
        def cvt_pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2597.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.PartToPartShearCouplingHalf)

        @property
        def pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2598.Pulley":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Pulley)

        @property
        def rolling_ring(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2604.RollingRing":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.RollingRing)

        @property
        def shaft_hub_connection(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2606.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.ShaftHubConnection)

        @property
        def spring_damper_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2609.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2613.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2613

            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2616.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2618.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2283.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2442.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2442.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)
