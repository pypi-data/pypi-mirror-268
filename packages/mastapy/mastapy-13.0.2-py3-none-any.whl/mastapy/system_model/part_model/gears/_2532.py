"""CylindricalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.gears import _2537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1016
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGear",)


Self = TypeVar("Self", bound="CylindricalGear")


class CylindricalGear(_2537.Gear):
    """CylindricalGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGear")

    class _Cast_CylindricalGear:
        """Special nested class for casting CylindricalGear to subclasses."""

        def __init__(
            self: "CylindricalGear._Cast_CylindricalGear", parent: "CylindricalGear"
        ):
            self._parent = parent

        @property
        def gear(self: "CylindricalGear._Cast_CylindricalGear") -> "_2537.Gear":
            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "CylindricalGear._Cast_CylindricalGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "CylindricalGear._Cast_CylindricalGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "CylindricalGear._Cast_CylindricalGear") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "CylindricalGear._Cast_CylindricalGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cylindrical_planet_gear(
            self: "CylindricalGear._Cast_CylindricalGear",
        ) -> "_2534.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.CylindricalPlanetGear)

        @property
        def cylindrical_gear(
            self: "CylindricalGear._Cast_CylindricalGear",
        ) -> "CylindricalGear":
            return self._parent

        def __getattr__(self: "CylindricalGear._Cast_CylindricalGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_of_estimated_micro_geometry_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance_to_tip_diameter_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClearanceToTipDiameterLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def clocking_angle_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClockingAngleError

        if temp is None:
            return 0.0

        return temp

    @clocking_angle_error.setter
    @enforce_parameter_types
    def clocking_angle_error(self: Self, value: "float"):
        self.wrapped.ClockingAngleError = float(value) if value is not None else 0.0

    @property
    def estimated_crowning(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EstimatedCrowning

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @estimated_crowning.setter
    @enforce_parameter_types
    def estimated_crowning(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EstimatedCrowning = value

    @property
    def extra_backlash(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ExtraBacklash

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @extra_backlash.setter
    @enforce_parameter_types
    def extra_backlash(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ExtraBacklash = value

    @property
    def has_concept_synchroniser(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasConceptSynchroniser

        if temp is None:
            return False

        return temp

    @has_concept_synchroniser.setter
    @enforce_parameter_types
    def has_concept_synchroniser(self: Self, value: "bool"):
        self.wrapped.HasConceptSynchroniser = (
            bool(value) if value is not None else False
        )

    @property
    def is_position_fixed_for_centre_distance_modification(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsPositionFixedForCentreDistanceModification

        if temp is None:
            return False

        return temp

    @is_position_fixed_for_centre_distance_modification.setter
    @enforce_parameter_types
    def is_position_fixed_for_centre_distance_modification(self: Self, value: "bool"):
        self.wrapped.IsPositionFixedForCentreDistanceModification = (
            bool(value) if value is not None else False
        )

    @property
    def left_limit_of_estimated_micro_geometry_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftLimitOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_relief(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LinearRelief

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @linear_relief.setter
    @enforce_parameter_types
    def linear_relief(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LinearRelief = value

    @property
    def minimum_rim_thickness_normal_module(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumRimThicknessNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_rim_thickness_normal_module.setter
    @enforce_parameter_types
    def minimum_rim_thickness_normal_module(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumRimThicknessNormalModule = value

    @property
    def reference_axis_angle_about_local_z_axis_from_y_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceAxisAngleAboutLocalZAxisFromYAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def right_limit_of_estimated_micro_geometry_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightLimitOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter_limit(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RootDiameterLimit

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @root_diameter_limit.setter
    @enforce_parameter_types
    def root_diameter_limit(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RootDiameterLimit = value

    @property
    def tip_diameter_limit(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TipDiameterLimit

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tip_diameter_limit.setter
    @enforce_parameter_types
    def tip_diameter_limit(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TipDiameterLimit = value

    @property
    def active_gear_design(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_meshes(self: Self) -> "List[_2316.CylindricalGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def make_carrier_assembly(
        self: Self,
        number_of_radial_bearings: "int",
        add_left_thrust_bearing: "bool",
        add_right_thrust_bearing: "bool",
        gear_bore: "float",
        carrier_bore: "float",
        carrier_width: "float",
        gear_offset: "float" = 0.0,
        left_bearing_indent: "float" = 0.0,
        right_bearing_indent: "float" = 0.0,
        thrust_pad_clearance: "float" = 0.0,
        adding_bearing: "bool" = True,
        left_thurst_pad_contact_diameter: Optional["Optional[float]"] = None,
        right_thurst_pad_contact_diameter: Optional["Optional[float]"] = None,
    ):
        """Method does not return.

        Args:
            number_of_radial_bearings (int)
            add_left_thrust_bearing (bool)
            add_right_thrust_bearing (bool)
            gear_bore (float)
            carrier_bore (float)
            carrier_width (float)
            gear_offset (float, optional)
            left_bearing_indent (float, optional)
            right_bearing_indent (float, optional)
            thrust_pad_clearance (float, optional)
            adding_bearing (bool, optional)
            left_thurst_pad_contact_diameter (Optional[float], optional)
            right_thurst_pad_contact_diameter (Optional[float], optional)
        """
        number_of_radial_bearings = int(number_of_radial_bearings)
        add_left_thrust_bearing = bool(add_left_thrust_bearing)
        add_right_thrust_bearing = bool(add_right_thrust_bearing)
        gear_bore = float(gear_bore)
        carrier_bore = float(carrier_bore)
        carrier_width = float(carrier_width)
        gear_offset = float(gear_offset)
        left_bearing_indent = float(left_bearing_indent)
        right_bearing_indent = float(right_bearing_indent)
        thrust_pad_clearance = float(thrust_pad_clearance)
        adding_bearing = bool(adding_bearing)
        self.wrapped.MakeCarrierAssembly(
            number_of_radial_bearings if number_of_radial_bearings else 0,
            add_left_thrust_bearing if add_left_thrust_bearing else False,
            add_right_thrust_bearing if add_right_thrust_bearing else False,
            gear_bore if gear_bore else 0.0,
            carrier_bore if carrier_bore else 0.0,
            carrier_width if carrier_width else 0.0,
            gear_offset if gear_offset else 0.0,
            left_bearing_indent if left_bearing_indent else 0.0,
            right_bearing_indent if right_bearing_indent else 0.0,
            thrust_pad_clearance if thrust_pad_clearance else 0.0,
            adding_bearing if adding_bearing else False,
            left_thurst_pad_contact_diameter,
            right_thurst_pad_contact_diameter,
        )

    @property
    def cast_to(self: Self) -> "CylindricalGear._Cast_CylindricalGear":
        return self._Cast_CylindricalGear(self)
