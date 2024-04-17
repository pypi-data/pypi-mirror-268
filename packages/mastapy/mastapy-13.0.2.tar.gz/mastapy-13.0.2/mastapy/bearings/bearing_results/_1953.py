"""LoadedBallElementChartReporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.bearings.bearing_results import _1969
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_ELEMENT_CHART_REPORTER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBallElementChartReporter"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1776, _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallElementChartReporter",)


Self = TypeVar("Self", bound="LoadedBallElementChartReporter")


class LoadedBallElementChartReporter(_1763.CustomReportChart):
    """LoadedBallElementChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_ELEMENT_CHART_REPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBallElementChartReporter")

    class _Cast_LoadedBallElementChartReporter:
        """Special nested class for casting LoadedBallElementChartReporter to subclasses."""

        def __init__(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
            parent: "LoadedBallElementChartReporter",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "_1763.CustomReportChart":
            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "_1776.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def loaded_ball_element_chart_reporter(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
        ) -> "LoadedBallElementChartReporter":
            return self._parent

        def __getattr__(
            self: "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBallElementChartReporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_to_plot(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.LoadedBallElementPropertyType]"""
        temp = self.wrapped.ElementToPlot

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @element_to_plot.setter
    @enforce_parameter_types
    def element_to_plot(self: Self, value: "_1969.LoadedBallElementPropertyType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ElementToPlot = value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter":
        return self._Cast_LoadedBallElementChartReporter(self)
