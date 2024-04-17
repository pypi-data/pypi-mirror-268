"""CustomReportChartItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportChartItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1756


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportChartItem",)


Self = TypeVar("Self", bound="CustomReportChartItem")


class CustomReportChartItem(_1780.CustomReportPropertyItem):
    """CustomReportChartItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportChartItem")

    class _Cast_CustomReportChartItem:
        """Special nested class for casting CustomReportChartItem to subclasses."""

        def __init__(
            self: "CustomReportChartItem._Cast_CustomReportChartItem",
            parent: "CustomReportChartItem",
        ):
            self._parent = parent

        @property
        def custom_report_property_item(
            self: "CustomReportChartItem._Cast_CustomReportChartItem",
        ) -> "_1780.CustomReportPropertyItem":
            return self._parent._cast(_1780.CustomReportPropertyItem)

        @property
        def custom_report_chart_item(
            self: "CustomReportChartItem._Cast_CustomReportChartItem",
        ) -> "CustomReportChartItem":
            return self._parent

        def __getattr__(
            self: "CustomReportChartItem._Cast_CustomReportChartItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportChartItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_marker(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasMarker

        if temp is None:
            return False

        return temp

    @has_marker.setter
    @enforce_parameter_types
    def has_marker(self: Self, value: "bool"):
        self.wrapped.HasMarker = bool(value) if value is not None else False

    @property
    def marker_size(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MarkerSize

        if temp is None:
            return 0.0

        return temp

    @marker_size.setter
    @enforce_parameter_types
    def marker_size(self: Self, value: "float"):
        self.wrapped.MarkerSize = float(value) if value is not None else 0.0

    @property
    def point_shape(self: Self) -> "_1756.SMTChartPointShape":
        """mastapy.utility.report.SMTChartPointShape"""
        temp = self.wrapped.PointShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.SMTChartPointShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.report._1756", "SMTChartPointShape"
        )(value)

    @point_shape.setter
    @enforce_parameter_types
    def point_shape(self: Self, value: "_1756.SMTChartPointShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.SMTChartPointShape"
        )
        self.wrapped.PointShape = value

    @property
    def smooth_lines(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SmoothLines

        if temp is None:
            return False

        return temp

    @smooth_lines.setter
    @enforce_parameter_types
    def smooth_lines(self: Self, value: "bool"):
        self.wrapped.SmoothLines = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomReportChartItem._Cast_CustomReportChartItem":
        return self._Cast_CustomReportChartItem(self)
