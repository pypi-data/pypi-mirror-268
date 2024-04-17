"""GearManufacturingConfigSetupViewModel"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.manufacturing.cylindrical import _626, _627
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIG_SETUP_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "GearManufacturingConfigSetupViewModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearManufacturingConfigSetupViewModel",)


Self = TypeVar("Self", bound="GearManufacturingConfigSetupViewModel")


class GearManufacturingConfigSetupViewModel(_0.APIBase):
    """GearManufacturingConfigSetupViewModel

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURING_CONFIG_SETUP_VIEW_MODEL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearManufacturingConfigSetupViewModel"
    )

    class _Cast_GearManufacturingConfigSetupViewModel:
        """Special nested class for casting GearManufacturingConfigSetupViewModel to subclasses."""

        def __init__(
            self: "GearManufacturingConfigSetupViewModel._Cast_GearManufacturingConfigSetupViewModel",
            parent: "GearManufacturingConfigSetupViewModel",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_config_setup_view_model(
            self: "GearManufacturingConfigSetupViewModel._Cast_GearManufacturingConfigSetupViewModel",
        ) -> "GearManufacturingConfigSetupViewModel":
            return self._parent

        def __getattr__(
            self: "GearManufacturingConfigSetupViewModel._Cast_GearManufacturingConfigSetupViewModel",
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
        self: Self, instance_to_wrap: "GearManufacturingConfigSetupViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_suitable_cutters(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateNewSuitableCutters

        if temp is None:
            return False

        return temp

    @create_new_suitable_cutters.setter
    @enforce_parameter_types
    def create_new_suitable_cutters(self: Self, value: "bool"):
        self.wrapped.CreateNewSuitableCutters = (
            bool(value) if value is not None else False
        )

    @property
    def finishing_method(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods"
    ):
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.CylindricalMftFinishingMethods]"""
        temp = self.wrapped.FinishingMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @finishing_method.setter
    @enforce_parameter_types
    def finishing_method(self: Self, value: "_626.CylindricalMftFinishingMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FinishingMethod = value

    @property
    def gear_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearName

        if temp is None:
            return ""

        return temp

    @property
    def rough_pressure_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RoughPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rough_pressure_angle.setter
    @enforce_parameter_types
    def rough_pressure_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RoughPressureAngle = value

    @property
    def roughing_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods]"""
        temp = self.wrapped.RoughingMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @roughing_method.setter
    @enforce_parameter_types
    def roughing_method(self: Self, value: "_627.CylindricalMftRoughingMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RoughingMethod = value

    @property
    def use_as_design_mode_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAsDesignModeGeometry

        if temp is None:
            return False

        return temp

    @use_as_design_mode_geometry.setter
    @enforce_parameter_types
    def use_as_design_mode_geometry(self: Self, value: "bool"):
        self.wrapped.UseAsDesignModeGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "GearManufacturingConfigSetupViewModel._Cast_GearManufacturingConfigSetupViewModel":
        return self._Cast_GearManufacturingConfigSetupViewModel(self)
