"""CustomReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.report import _1752, _1771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT = python_net_import("SMT.MastaAPI.Utility.Report", "CustomReport")

if TYPE_CHECKING:
    from mastapy.utility.report import _1754, _1788, _1753, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReport",)


Self = TypeVar("Self", bound="CustomReport")


class CustomReport(_1771.CustomReportItemContainer):
    """CustomReport

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReport")

    class _Cast_CustomReport:
        """Special nested class for casting CustomReport to subclasses."""

        def __init__(self: "CustomReport._Cast_CustomReport", parent: "CustomReport"):
            self._parent = parent

        @property
        def custom_report_item_container(
            self: "CustomReport._Cast_CustomReport",
        ) -> "_1771.CustomReportItemContainer":
            return self._parent._cast(_1771.CustomReportItemContainer)

        @property
        def custom_report_item(
            self: "CustomReport._Cast_CustomReport",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report(self: "CustomReport._Cast_CustomReport") -> "CustomReport":
            return self._parent

        def __getattr__(self: "CustomReport._Cast_CustomReport", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_table_border_style(self: Self) -> "_1754.CadTableBorderType":
        """mastapy.utility.report.CadTableBorderType"""
        temp = self.wrapped.CADTableBorderStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.CadTableBorderType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1754", "CadTableBorderType"
        )(value)

    @cad_table_border_style.setter
    @enforce_parameter_types
    def cad_table_border_style(self: Self, value: "_1754.CadTableBorderType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.CadTableBorderType"
        )
        self.wrapped.CADTableBorderStyle = value

    @property
    def font_height_for_cad_tables(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FontHeightForCADTables

        if temp is None:
            return 0.0

        return temp

    @font_height_for_cad_tables.setter
    @enforce_parameter_types
    def font_height_for_cad_tables(self: Self, value: "float"):
        self.wrapped.FontHeightForCADTables = float(value) if value is not None else 0.0

    @property
    def hide_cad_table_borders(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HideCADTableBorders

        if temp is None:
            return False

        return temp

    @hide_cad_table_borders.setter
    @enforce_parameter_types
    def hide_cad_table_borders(self: Self, value: "bool"):
        self.wrapped.HideCADTableBorders = bool(value) if value is not None else False

    @property
    def include_report_check(self: Self) -> "_1788.DefinitionBooleanCheckOptions":
        """mastapy.utility.report.DefinitionBooleanCheckOptions"""
        temp = self.wrapped.IncludeReportCheck

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.DefinitionBooleanCheckOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1788", "DefinitionBooleanCheckOptions"
        )(value)

    @include_report_check.setter
    @enforce_parameter_types
    def include_report_check(self: Self, value: "_1788.DefinitionBooleanCheckOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.DefinitionBooleanCheckOptions"
        )
        self.wrapped.IncludeReportCheck = value

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
    def page_height_for_cad_export(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PageHeightForCADExport

        if temp is None:
            return 0.0

        return temp

    @page_height_for_cad_export.setter
    @enforce_parameter_types
    def page_height_for_cad_export(self: Self, value: "float"):
        self.wrapped.PageHeightForCADExport = float(value) if value is not None else 0.0

    @property
    def page_orientation_for_cad_export(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation":
        """EnumWithSelectedValue[mastapy.utility.report.CadPageOrientation]"""
        temp = self.wrapped.PageOrientationForCADExport

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @page_orientation_for_cad_export.setter
    @enforce_parameter_types
    def page_orientation_for_cad_export(self: Self, value: "_1752.CadPageOrientation"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PageOrientationForCADExport = value

    @property
    def page_size_for_cad_export(self: Self) -> "_1753.CadPageSize":
        """mastapy.utility.report.CadPageSize"""
        temp = self.wrapped.PageSizeForCADExport

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.CadPageSize"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1753", "CadPageSize"
        )(value)

    @page_size_for_cad_export.setter
    @enforce_parameter_types
    def page_size_for_cad_export(self: Self, value: "_1753.CadPageSize"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.CadPageSize"
        )
        self.wrapped.PageSizeForCADExport = value

    @property
    def page_width_for_cad_export(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PageWidthForCADExport

        if temp is None:
            return 0.0

        return temp

    @page_width_for_cad_export.setter
    @enforce_parameter_types
    def page_width_for_cad_export(self: Self, value: "float"):
        self.wrapped.PageWidthForCADExport = float(value) if value is not None else 0.0

    @property
    def show_table_of_contents(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTableOfContents

        if temp is None:
            return False

        return temp

    @show_table_of_contents.setter
    @enforce_parameter_types
    def show_table_of_contents(self: Self, value: "bool"):
        self.wrapped.ShowTableOfContents = bool(value) if value is not None else False

    @property
    def text_margin_for_cad_tables(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TextMarginForCADTables

        if temp is None:
            return 0.0

        return temp

    @text_margin_for_cad_tables.setter
    @enforce_parameter_types
    def text_margin_for_cad_tables(self: Self, value: "float"):
        self.wrapped.TextMarginForCADTables = float(value) if value is not None else 0.0

    @property
    def use_default_border(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultBorder

        if temp is None:
            return False

        return temp

    @use_default_border.setter
    @enforce_parameter_types
    def use_default_border(self: Self, value: "bool"):
        self.wrapped.UseDefaultBorder = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomReport._Cast_CustomReport":
        return self._Cast_CustomReport(self)
