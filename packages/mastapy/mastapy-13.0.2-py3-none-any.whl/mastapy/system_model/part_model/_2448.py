"""BearingRaceMountingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.bearings.bearing_results import _1970, _1971
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_BEARING_RACE_MOUNTING_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "BearingRaceMountingOptions"
)

if TYPE_CHECKING:
    from mastapy.materials import _248
    from mastapy.system_model.part_model import _2465, _2474


__docformat__ = "restructuredtext en"
__all__ = ("BearingRaceMountingOptions",)


Self = TypeVar("Self", bound="BearingRaceMountingOptions")


class BearingRaceMountingOptions(_0.APIBase):
    """BearingRaceMountingOptions

    This is a mastapy class.
    """

    TYPE = _BEARING_RACE_MOUNTING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingRaceMountingOptions")

    class _Cast_BearingRaceMountingOptions:
        """Special nested class for casting BearingRaceMountingOptions to subclasses."""

        def __init__(
            self: "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions",
            parent: "BearingRaceMountingOptions",
        ):
            self._parent = parent

        @property
        def inner_bearing_race_mounting_options(
            self: "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions",
        ) -> "_2465.InnerBearingRaceMountingOptions":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.InnerBearingRaceMountingOptions)

        @property
        def outer_bearing_race_mounting_options(
            self: "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions",
        ) -> "_2474.OuterBearingRaceMountingOptions":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.OuterBearingRaceMountingOptions)

        @property
        def bearing_race_mounting_options(
            self: "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions",
        ) -> "BearingRaceMountingOptions":
            return self._parent

        def __getattr__(
            self: "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingRaceMountingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_mounting(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RaceAxialMountingType":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.RaceAxialMountingType]"""
        temp = self.wrapped.AxialMounting

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RaceAxialMountingType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @axial_mounting.setter
    @enforce_parameter_types
    def axial_mounting(self: Self, value: "_1970.RaceAxialMountingType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RaceAxialMountingType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AxialMounting = value

    @property
    def bore_mounting_sleeve(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BoreMountingSleeve

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bore_mounting_sleeve.setter
    @enforce_parameter_types
    def bore_mounting_sleeve(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BoreMountingSleeve = value

    @property
    def has_mounting_sleeve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasMountingSleeve

        if temp is None:
            return False

        return temp

    @has_mounting_sleeve.setter
    @enforce_parameter_types
    def has_mounting_sleeve(self: Self, value: "bool"):
        self.wrapped.HasMountingSleeve = bool(value) if value is not None else False

    @property
    def left_axial_mounting_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftAxialMountingClearance

        if temp is None:
            return 0.0

        return temp

    @left_axial_mounting_clearance.setter
    @enforce_parameter_types
    def left_axial_mounting_clearance(self: Self, value: "float"):
        self.wrapped.LeftAxialMountingClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def mounting_sleeve_material_reportable(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MountingSleeveMaterialReportable.SelectedItemName

        if temp is None:
            return ""

        return temp

    @mounting_sleeve_material_reportable.setter
    @enforce_parameter_types
    def mounting_sleeve_material_reportable(self: Self, value: "str"):
        self.wrapped.MountingSleeveMaterialReportable.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def outer_diameter_mounting_sleeve(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterDiameterMountingSleeve

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_diameter_mounting_sleeve.setter
    @enforce_parameter_types
    def outer_diameter_mounting_sleeve(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterDiameterMountingSleeve = value

    @property
    def radial_clearance_contact_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialClearanceContactStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_clearance_contact_stiffness.setter
    @enforce_parameter_types
    def radial_clearance_contact_stiffness(self: Self, value: "float"):
        self.wrapped.RadialClearanceContactStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def radial_mounting_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialMountingClearance

        if temp is None:
            return 0.0

        return temp

    @radial_mounting_clearance.setter
    @enforce_parameter_types
    def radial_mounting_clearance(self: Self, value: "float"):
        self.wrapped.RadialMountingClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def right_axial_mounting_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightAxialMountingClearance

        if temp is None:
            return 0.0

        return temp

    @right_axial_mounting_clearance.setter
    @enforce_parameter_types
    def right_axial_mounting_clearance(self: Self, value: "float"):
        self.wrapped.RightAxialMountingClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def simple_radial_mounting(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RaceRadialMountingType":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.RaceRadialMountingType]"""
        temp = self.wrapped.SimpleRadialMounting

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RaceRadialMountingType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @simple_radial_mounting.setter
    @enforce_parameter_types
    def simple_radial_mounting(self: Self, value: "_1971.RaceRadialMountingType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RaceRadialMountingType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SimpleRadialMounting = value

    @property
    def temperature_of_mounting_sleeve(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TemperatureOfMountingSleeve

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @temperature_of_mounting_sleeve.setter
    @enforce_parameter_types
    def temperature_of_mounting_sleeve(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TemperatureOfMountingSleeve = value

    @property
    def mounting_sleeve_material(self: Self) -> "_248.BearingMaterial":
        """mastapy.materials.BearingMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MountingSleeveMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BearingRaceMountingOptions._Cast_BearingRaceMountingOptions":
        return self._Cast_BearingRaceMountingOptions(self)
