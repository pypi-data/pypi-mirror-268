"""Component"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._math.vector_3d import Vector3D
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2475
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from mastapy.math_utility import _1506, _1507
    from mastapy.system_model.connections_and_sockets import _2277, _2279, _2303, _2298
    from mastapy.system_model.part_model import (
        _2452,
        _2442,
        _2443,
        _2446,
        _2449,
        _2454,
        _2455,
        _2459,
        _2460,
        _2462,
        _2469,
        _2470,
        _2471,
        _2473,
        _2476,
        _2478,
        _2479,
        _2484,
        _2486,
    )
    from mastapy.system_model.part_model.shaft_model import _2489
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
    from mastapy.system_model.part_model.cycloidal import _2576, _2577
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
__all__ = ("Component",)


Self = TypeVar("Self", bound="Component")


class Component(_2475.Part):
    """Component

    This is a mastapy class.
    """

    TYPE = _COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Component")

    class _Cast_Component:
        """Special nested class for casting Component to subclasses."""

        def __init__(self: "Component._Cast_Component", parent: "Component"):
            self._parent = parent

        @property
        def part(self: "Component._Cast_Component") -> "_2475.Part":
            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Component._Cast_Component") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def abstract_shaft(self: "Component._Cast_Component") -> "_2442.AbstractShaft":
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "Component._Cast_Component",
        ) -> "_2443.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.AbstractShaftOrHousing)

        @property
        def bearing(self: "Component._Cast_Component") -> "_2446.Bearing":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Bearing)

        @property
        def bolt(self: "Component._Cast_Component") -> "_2449.Bolt":
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.Bolt)

        @property
        def connector(self: "Component._Cast_Component") -> "_2454.Connector":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.Connector)

        @property
        def datum(self: "Component._Cast_Component") -> "_2455.Datum":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.Datum)

        @property
        def external_cad_model(
            self: "Component._Cast_Component",
        ) -> "_2459.ExternalCADModel":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.ExternalCADModel)

        @property
        def fe_part(self: "Component._Cast_Component") -> "_2460.FEPart":
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.FEPart)

        @property
        def guide_dxf_model(self: "Component._Cast_Component") -> "_2462.GuideDxfModel":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.GuideDxfModel)

        @property
        def mass_disc(self: "Component._Cast_Component") -> "_2469.MassDisc":
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.MassDisc)

        @property
        def measurement_component(
            self: "Component._Cast_Component",
        ) -> "_2470.MeasurementComponent":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.MeasurementComponent)

        @property
        def mountable_component(
            self: "Component._Cast_Component",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def oil_seal(self: "Component._Cast_Component") -> "_2473.OilSeal":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.OilSeal)

        @property
        def planet_carrier(self: "Component._Cast_Component") -> "_2476.PlanetCarrier":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.PlanetCarrier)

        @property
        def point_load(self: "Component._Cast_Component") -> "_2478.PointLoad":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.PointLoad)

        @property
        def power_load(self: "Component._Cast_Component") -> "_2479.PowerLoad":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.PowerLoad)

        @property
        def unbalanced_mass(
            self: "Component._Cast_Component",
        ) -> "_2484.UnbalancedMass":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.UnbalancedMass)

        @property
        def virtual_component(
            self: "Component._Cast_Component",
        ) -> "_2486.VirtualComponent":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.VirtualComponent)

        @property
        def shaft(self: "Component._Cast_Component") -> "_2489.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2489

            return self._parent._cast(_2489.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "Component._Cast_Component",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "Component._Cast_Component",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "Component._Cast_Component",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "Component._Cast_Component",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Component._Cast_Component") -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def concept_gear(self: "Component._Cast_Component") -> "_2528.ConceptGear":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.ConceptGear)

        @property
        def conical_gear(self: "Component._Cast_Component") -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def cylindrical_gear(
            self: "Component._Cast_Component",
        ) -> "_2532.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "Component._Cast_Component",
        ) -> "_2534.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.CylindricalPlanetGear)

        @property
        def face_gear(self: "Component._Cast_Component") -> "_2535.FaceGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.FaceGear)

        @property
        def gear(self: "Component._Cast_Component") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def hypoid_gear(self: "Component._Cast_Component") -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "Component._Cast_Component",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "Component._Cast_Component",
        ) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Component._Cast_Component",
        ) -> "_2547.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "Component._Cast_Component",
        ) -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "Component._Cast_Component",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "Component._Cast_Component",
        ) -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "Component._Cast_Component",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "Component._Cast_Component",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def worm_gear(self: "Component._Cast_Component") -> "_2558.WormGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.WormGear)

        @property
        def zerol_bevel_gear(
            self: "Component._Cast_Component",
        ) -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def cycloidal_disc(self: "Component._Cast_Component") -> "_2576.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2576

            return self._parent._cast(_2576.CycloidalDisc)

        @property
        def ring_pins(self: "Component._Cast_Component") -> "_2577.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2577

            return self._parent._cast(_2577.RingPins)

        @property
        def clutch_half(self: "Component._Cast_Component") -> "_2586.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "Component._Cast_Component",
        ) -> "_2589.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.ConceptCouplingHalf)

        @property
        def coupling_half(self: "Component._Cast_Component") -> "_2592.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.CouplingHalf)

        @property
        def cvt_pulley(self: "Component._Cast_Component") -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "Component._Cast_Component",
        ) -> "_2597.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Component._Cast_Component") -> "_2598.Pulley":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Pulley)

        @property
        def rolling_ring(self: "Component._Cast_Component") -> "_2604.RollingRing":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.RollingRing)

        @property
        def shaft_hub_connection(
            self: "Component._Cast_Component",
        ) -> "_2606.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.ShaftHubConnection)

        @property
        def spring_damper_half(
            self: "Component._Cast_Component",
        ) -> "_2609.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "Component._Cast_Component",
        ) -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "Component._Cast_Component",
        ) -> "_2613.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2613

            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "Component._Cast_Component",
        ) -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "Component._Cast_Component",
        ) -> "_2616.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "Component._Cast_Component",
        ) -> "_2618.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.TorqueConverterTurbine)

        @property
        def component(self: "Component._Cast_Component") -> "Component":
            return self._parent

        def __getattr__(self: "Component._Cast_Component", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Component.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def polar_inertia(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia.setter
    @enforce_parameter_types
    def polar_inertia(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertia = value

    @property
    def polar_inertia_for_synchroniser_sizing_only(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertiaForSynchroniserSizingOnly

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia_for_synchroniser_sizing_only.setter
    @enforce_parameter_types
    def polar_inertia_for_synchroniser_sizing_only(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertiaForSynchroniserSizingOnly = value

    @property
    def reason_mass_properties_are_unknown(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ""

        return temp

    @property
    def translation(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Translation

        if temp is None:
            return ""

        return temp

    @property
    def transverse_inertia(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TransverseInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_inertia.setter
    @enforce_parameter_types
    def transverse_inertia(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TransverseInertia = value

    @property
    def x_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxis

        if temp is None:
            return ""

        return temp

    @property
    def y_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxis

        if temp is None:
            return ""

        return temp

    @property
    def z_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxis

        if temp is None:
            return ""

        return temp

    @property
    def coordinate_system_euler_angles(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.CoordinateSystemEulerAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @coordinate_system_euler_angles.setter
    @enforce_parameter_types
    def coordinate_system_euler_angles(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.CoordinateSystemEulerAngles = value

    @property
    def local_coordinate_system(self: Self) -> "_1506.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position.setter
    @enforce_parameter_types
    def position(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Position = value

    @property
    def component_connections(self: Self) -> "List[_2277.ComponentConnection]":
        """List[mastapy.system_model.connections_and_sockets.ComponentConnection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def available_socket_offsets(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableSocketOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def centre_offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOffset

        if temp is None:
            return 0.0

        return temp

    @property
    def translation_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TranslationVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def x_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def y_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def z_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def can_connect_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.CanConnectTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def can_delete_connection(self: Self, connection: "_2279.Connection") -> "bool":
        """bool

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.CanDeleteConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def connect_to(
        self: Self, component: "Component"
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: Self, socket: "_2303.Socket"
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_coordinate_system_editor(self: Self) -> "_1507.CoordinateSystemEditor":
        """mastapy.math_utility.CoordinateSystemEditor"""
        method_result = self.wrapped.CreateCoordinateSystemEditor()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def diameter_at_middle_of_connection(
        self: Self, connection: "_2279.Connection"
    ) -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterAtMiddleOfConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def diameter_of_socket_for(self: Self, connection: "_2279.Connection") -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterOfSocketFor(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def is_coaxially_connected_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsCoaxiallyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_connected_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_or_indirectly_connected_to(
        self: Self, component: "Component"
    ) -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyOrIndirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def move_all_concentric_parts_radially(
        self: Self, delta_x: "float", delta_y: "float"
    ) -> "bool":
        """bool

        Args:
            delta_x (float)
            delta_y (float)
        """
        delta_x = float(delta_x)
        delta_y = float(delta_y)
        method_result = self.wrapped.MoveAllConcentricPartsRadially(
            delta_x if delta_x else 0.0, delta_y if delta_y else 0.0
        )
        return method_result

    @enforce_parameter_types
    def move_along_axis(self: Self, delta: "float"):
        """Method does not return.

        Args:
            delta (float)
        """
        delta = float(delta)
        self.wrapped.MoveAlongAxis(delta if delta else 0.0)

    @enforce_parameter_types
    def move_with_concentric_parts_to_new_origin(
        self: Self, target_origin: "Vector3D"
    ) -> "bool":
        """bool

        Args:
            target_origin (Vector3D)
        """
        target_origin = conversion.mp_to_pn_vector3d(target_origin)
        method_result = self.wrapped.MoveWithConcentricPartsToNewOrigin(target_origin)
        return method_result

    @enforce_parameter_types
    def possible_sockets_to_connect_with_component(
        self: Self, component: "Component"
    ) -> "List[_2303.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_COMPONENT](
                component.wrapped if component else None
            )
        )

    @enforce_parameter_types
    def possible_sockets_to_connect_with(
        self: Self, socket: "_2303.Socket"
    ) -> "List[_2303.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_SOCKET](
                socket.wrapped if socket else None
            )
        )

    @enforce_parameter_types
    def set_position_and_axis_of_component_and_connected_components(
        self: Self, origin: "Vector3D", z_axis: "Vector3D"
    ) -> "_2298.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            origin (Vector3D)
            z_axis (Vector3D)
        """
        origin = conversion.mp_to_pn_vector3d(origin)
        z_axis = conversion.mp_to_pn_vector3d(z_axis)
        method_result = (
            self.wrapped.SetPositionAndAxisOfComponentAndConnectedComponents(
                origin, z_axis
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_and_rotation_of_component_and_connected_components(
        self: Self, new_coordinate_system: "_1506.CoordinateSystem3D"
    ) -> "_2298.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            new_coordinate_system (mastapy.math_utility.CoordinateSystem3D)
        """
        method_result = (
            self.wrapped.SetPositionAndRotationOfComponentAndConnectedComponents(
                new_coordinate_system.wrapped if new_coordinate_system else None
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_of_component_and_connected_components(
        self: Self, position: "Vector3D"
    ) -> "_2298.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            position (Vector3D)
        """
        position = conversion.mp_to_pn_vector3d(position)
        method_result = self.wrapped.SetPositionOfComponentAndConnectedComponents(
            position
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_named(self: Self, socket_name: "str") -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket_name (str)
        """
        socket_name = str(socket_name)
        method_result = self.wrapped.SocketNamed(socket_name if socket_name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_connect_to(
        self: Self, component: "Component", hint_offset: "float" = float("nan")
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
            hint_offset (float, optional)
        """
        hint_offset = float(hint_offset)
        method_result = self.wrapped.TryConnectTo(
            component.wrapped if component else None,
            hint_offset if hint_offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Component._Cast_Component":
        return self._Cast_Component(self)
