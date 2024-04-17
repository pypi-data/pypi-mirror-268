"""LoadedBearingChartReporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_CHART_REPORTER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingChartReporter"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1759, _1767, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBearingChartReporter",)


Self = TypeVar("Self", bound="LoadedBearingChartReporter")


class LoadedBearingChartReporter(_1760.CustomImage):
    """LoadedBearingChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_CHART_REPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBearingChartReporter")

    class _Cast_LoadedBearingChartReporter:
        """Special nested class for casting LoadedBearingChartReporter to subclasses."""

        def __init__(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
            parent: "LoadedBearingChartReporter",
        ):
            self._parent = parent

        @property
        def custom_image(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "_1760.CustomImage":
            return self._parent._cast(_1760.CustomImage)

        @property
        def custom_graphic(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "_1759.CustomGraphic":
            from mastapy.utility.report import _1759

            return self._parent._cast(_1759.CustomGraphic)

        @property
        def custom_report_definition_item(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "_1767.CustomReportDefinitionItem":
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def loaded_bearing_chart_reporter(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
        ) -> "LoadedBearingChartReporter":
            return self._parent

        def __getattr__(
            self: "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBearingChartReporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def property_(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Property

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @property_.setter
    @enforce_parameter_types
    def property_(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Property = value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedBearingChartReporter._Cast_LoadedBearingChartReporter":
        return self._Cast_LoadedBearingChartReporter(self)
