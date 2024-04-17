"""CylindricalGearCuttingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.gears.gear_designs.cylindrical import _1054
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CUTTING_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearCuttingOptions"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1010, _1035
    from mastapy.gears.manufacturing.cylindrical import _615


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCuttingOptions",)


Self = TypeVar("Self", bound="CylindricalGearCuttingOptions")


class CylindricalGearCuttingOptions(_0.APIBase):
    """CylindricalGearCuttingOptions

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CUTTING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearCuttingOptions")

    class _Cast_CylindricalGearCuttingOptions:
        """Special nested class for casting CylindricalGearCuttingOptions to subclasses."""

        def __init__(
            self: "CylindricalGearCuttingOptions._Cast_CylindricalGearCuttingOptions",
            parent: "CylindricalGearCuttingOptions",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_cutting_options(
            self: "CylindricalGearCuttingOptions._Cast_CylindricalGearCuttingOptions",
        ) -> "CylindricalGearCuttingOptions":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCuttingOptions._Cast_CylindricalGearCuttingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearCuttingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_specification_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.cylindrical.GeometrySpecificationType]"""
        temp = self.wrapped.GeometrySpecificationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @geometry_specification_type.setter
    @enforce_parameter_types
    def geometry_specification_type(
        self: Self, value: "_1054.GeometrySpecificationType"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.GeometrySpecificationType = value

    @property
    def thickness_for_analyses(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ThicknessForAnalyses

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @thickness_for_analyses.setter
    @enforce_parameter_types
    def thickness_for_analyses(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ThicknessForAnalyses = value

    @property
    def use_design_default_toleranced_measurement(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignDefaultTolerancedMeasurement

        if temp is None:
            return False

        return temp

    @use_design_default_toleranced_measurement.setter
    @enforce_parameter_types
    def use_design_default_toleranced_measurement(self: Self, value: "bool"):
        self.wrapped.UseDesignDefaultTolerancedMeasurement = (
            bool(value) if value is not None else False
        )

    @property
    def cylindrical_gear_cutter(self: Self) -> "_1010.CylindricalGearAbstractRack":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearAbstractRack

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def manufacturing_configuration(
        self: Self,
    ) -> "_615.CylindricalGearManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def manufacturing_configuration_selection(
        self: Self,
    ) -> "_1035.CylindricalGearSetManufacturingConfigurationSelection":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetManufacturingConfigurationSelection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfigurationSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCuttingOptions._Cast_CylindricalGearCuttingOptions":
        return self._Cast_CylindricalGearCuttingOptions(self)
