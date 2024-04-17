"""CustomChart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_CHART = python_net_import("SMT.MastaAPI.Utility.Report", "CustomChart")

if TYPE_CHECKING:
    from mastapy.utility.report import _1767, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomChart",)


Self = TypeVar("Self", bound="CustomChart")


class CustomChart(_1759.CustomGraphic):
    """CustomChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomChart")

    class _Cast_CustomChart:
        """Special nested class for casting CustomChart to subclasses."""

        def __init__(self: "CustomChart._Cast_CustomChart", parent: "CustomChart"):
            self._parent = parent

        @property
        def custom_graphic(
            self: "CustomChart._Cast_CustomChart",
        ) -> "_1759.CustomGraphic":
            return self._parent._cast(_1759.CustomGraphic)

        @property
        def custom_report_definition_item(
            self: "CustomChart._Cast_CustomChart",
        ) -> "_1767.CustomReportDefinitionItem":
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomChart._Cast_CustomChart",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomChart._Cast_CustomChart",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_chart(self: "CustomChart._Cast_CustomChart") -> "CustomChart":
            return self._parent

        def __getattr__(self: "CustomChart._Cast_CustomChart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def line_thickness_factor(self: Self) -> "int":
        """int"""
        temp = self.wrapped.LineThicknessFactor

        if temp is None:
            return 0

        return temp

    @line_thickness_factor.setter
    @enforce_parameter_types
    def line_thickness_factor(self: Self, value: "int"):
        self.wrapped.LineThicknessFactor = int(value) if value is not None else 0

    @property
    def show_header(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowHeader

        if temp is None:
            return False

        return temp

    @show_header.setter
    @enforce_parameter_types
    def show_header(self: Self, value: "bool"):
        self.wrapped.ShowHeader = bool(value) if value is not None else False

    @property
    def text_is_uppercase(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TextIsUppercase

        if temp is None:
            return False

        return temp

    @text_is_uppercase.setter
    @enforce_parameter_types
    def text_is_uppercase(self: Self, value: "bool"):
        self.wrapped.TextIsUppercase = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomChart._Cast_CustomChart":
        return self._Cast_CustomChart(self)
