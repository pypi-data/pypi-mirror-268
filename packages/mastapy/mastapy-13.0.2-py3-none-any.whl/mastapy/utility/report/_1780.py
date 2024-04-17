"""CustomReportPropertyItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_PROPERTY_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportPropertyItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1790, _1791, _1751, _1764, _1785, _1794
    from mastapy.utility.reporting_property_framework import _1795


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportPropertyItem",)


Self = TypeVar("Self", bound="CustomReportPropertyItem")


class CustomReportPropertyItem(_0.APIBase):
    """CustomReportPropertyItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_PROPERTY_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportPropertyItem")

    class _Cast_CustomReportPropertyItem:
        """Special nested class for casting CustomReportPropertyItem to subclasses."""

        def __init__(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
            parent: "CustomReportPropertyItem",
        ):
            self._parent = parent

        @property
        def blank_row(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
        ) -> "_1751.BlankRow":
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.BlankRow)

        @property
        def custom_report_chart_item(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
        ) -> "_1764.CustomReportChartItem":
            from mastapy.utility.report import _1764

            return self._parent._cast(_1764.CustomReportChartItem)

        @property
        def custom_row(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
        ) -> "_1785.CustomRow":
            from mastapy.utility.report import _1785

            return self._parent._cast(_1785.CustomRow)

        @property
        def user_text_row(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
        ) -> "_1794.UserTextRow":
            from mastapy.utility.report import _1794

            return self._parent._cast(_1794.UserTextRow)

        @property
        def custom_report_property_item(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem",
        ) -> "CustomReportPropertyItem":
            return self._parent

        def __getattr__(
            self: "CustomReportPropertyItem._Cast_CustomReportPropertyItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportPropertyItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def font_style(self: Self) -> "_1790.FontStyle":
        """mastapy.utility.report.FontStyle"""
        temp = self.wrapped.FontStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Utility.Report.FontStyle")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1790", "FontStyle"
        )(value)

    @font_style.setter
    @enforce_parameter_types
    def font_style(self: Self, value: "_1790.FontStyle"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Utility.Report.FontStyle")
        self.wrapped.FontStyle = value

    @property
    def font_weight(self: Self) -> "_1791.FontWeight":
        """mastapy.utility.report.FontWeight"""
        temp = self.wrapped.FontWeight

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Utility.Report.FontWeight")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1791", "FontWeight"
        )(value)

    @font_weight.setter
    @enforce_parameter_types
    def font_weight(self: Self, value: "_1791.FontWeight"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.FontWeight"
        )
        self.wrapped.FontWeight = value

    @property
    def horizontal_position(self: Self) -> "_1795.CellValuePosition":
        """mastapy.utility.reporting_property_framework.CellValuePosition"""
        temp = self.wrapped.HorizontalPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.ReportingPropertyFramework.CellValuePosition"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.reporting_property_framework._1795", "CellValuePosition"
        )(value)

    @horizontal_position.setter
    @enforce_parameter_types
    def horizontal_position(self: Self, value: "_1795.CellValuePosition"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.ReportingPropertyFramework.CellValuePosition"
        )
        self.wrapped.HorizontalPosition = value

    @property
    def show_property_name(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowPropertyName

        if temp is None:
            return False

        return temp

    @show_property_name.setter
    @enforce_parameter_types
    def show_property_name(self: Self, value: "bool"):
        self.wrapped.ShowPropertyName = bool(value) if value is not None else False

    def add_condition(self: Self):
        """Method does not return."""
        self.wrapped.AddCondition()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportPropertyItem._Cast_CustomReportPropertyItem":
        return self._Cast_CustomReportPropertyItem(self)
