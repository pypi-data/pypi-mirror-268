"""ShaftSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.python_net import python_net_import
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.shafts import _34
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_SHAFT_SETTINGS_ITEM = python_net_import("SMT.MastaAPI.Shafts", "ShaftSettingsItem")

if TYPE_CHECKING:
    from mastapy.shafts import _13


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSettingsItem",)


Self = TypeVar("Self", bound="ShaftSettingsItem")


class ShaftSettingsItem(_1836.NamedDatabaseItem):
    """ShaftSettingsItem

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSettingsItem")

    class _Cast_ShaftSettingsItem:
        """Special nested class for casting ShaftSettingsItem to subclasses."""

        def __init__(
            self: "ShaftSettingsItem._Cast_ShaftSettingsItem",
            parent: "ShaftSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "ShaftSettingsItem._Cast_ShaftSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def shaft_settings_item(
            self: "ShaftSettingsItem._Cast_ShaftSettingsItem",
        ) -> "ShaftSettingsItem":
            return self._parent

        def __getattr__(self: "ShaftSettingsItem._Cast_ShaftSettingsItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSettingsItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_assembly_by_default_when_adding_part_via_dxf(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateNewAssemblyByDefaultWhenAddingPartViaDXF

        if temp is None:
            return False

        return temp

    @create_new_assembly_by_default_when_adding_part_via_dxf.setter
    @enforce_parameter_types
    def create_new_assembly_by_default_when_adding_part_via_dxf(
        self: Self, value: "bool"
    ):
        self.wrapped.CreateNewAssemblyByDefaultWhenAddingPartViaDXF = (
            bool(value) if value is not None else False
        )

    @property
    def material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @material_database.setter
    @enforce_parameter_types
    def material_database(self: Self, value: "str"):
        self.wrapped.MaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def reliability_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliabilityFactor

        if temp is None:
            return 0.0

        return temp

    @reliability_factor.setter
    @enforce_parameter_types
    def reliability_factor(self: Self, value: "float"):
        self.wrapped.ReliabilityFactor = float(value) if value is not None else 0.0

    @property
    def required_shaft_reliability(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredShaftReliability

        if temp is None:
            return 0.0

        return temp

    @required_shaft_reliability.setter
    @enforce_parameter_types
    def required_shaft_reliability(self: Self, value: "float"):
        self.wrapped.RequiredShaftReliability = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaft_rating_method(self: Self) -> "_34.ShaftRatingMethod":
        """mastapy.shafts.ShaftRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Shafts.ShaftRatingMethod")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.shafts._34", "ShaftRatingMethod")(
            value
        )

    @property
    def shaft_rating_method_selector(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShaftRatingMethod":
        """EnumWithSelectedValue[mastapy.shafts.ShaftRatingMethod]"""
        temp = self.wrapped.ShaftRatingMethodSelector

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftRatingMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @shaft_rating_method_selector.setter
    @enforce_parameter_types
    def shaft_rating_method_selector(self: Self, value: "_34.ShaftRatingMethod"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftRatingMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftRatingMethodSelector = value

    @property
    def version_of_miners_rule(self: Self) -> "_13.FkmVersionOfMinersRule":
        """mastapy.shafts.FkmVersionOfMinersRule"""
        temp = self.wrapped.VersionOfMinersRule

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Shafts.FkmVersionOfMinersRule"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.shafts._13", "FkmVersionOfMinersRule"
        )(value)

    @version_of_miners_rule.setter
    @enforce_parameter_types
    def version_of_miners_rule(self: Self, value: "_13.FkmVersionOfMinersRule"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Shafts.FkmVersionOfMinersRule"
        )
        self.wrapped.VersionOfMinersRule = value

    @property
    def cast_to(self: Self) -> "ShaftSettingsItem._Cast_ShaftSettingsItem":
        return self._Cast_ShaftSettingsItem(self)
