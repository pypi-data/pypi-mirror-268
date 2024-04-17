"""WaterfallChartSettings"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WATERFALL_CHART_SETTINGS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "WaterfallChartSettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("WaterfallChartSettings",)


Self = TypeVar("Self", bound="WaterfallChartSettings")


class WaterfallChartSettings(_0.APIBase):
    """WaterfallChartSettings

    This is a mastapy class.
    """

    TYPE = _WATERFALL_CHART_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WaterfallChartSettings")

    class _Cast_WaterfallChartSettings:
        """Special nested class for casting WaterfallChartSettings to subclasses."""

        def __init__(
            self: "WaterfallChartSettings._Cast_WaterfallChartSettings",
            parent: "WaterfallChartSettings",
        ):
            self._parent = parent

        @property
        def waterfall_chart_settings(
            self: "WaterfallChartSettings._Cast_WaterfallChartSettings",
        ) -> "WaterfallChartSettings":
            return self._parent

        def __getattr__(
            self: "WaterfallChartSettings._Cast_WaterfallChartSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WaterfallChartSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def three_d_view(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ThreeDView

        if temp is None:
            return False

        return temp

    @three_d_view.setter
    @enforce_parameter_types
    def three_d_view(self: Self, value: "bool"):
        self.wrapped.ThreeDView = bool(value) if value is not None else False

    @property
    def draw_lines_on_top_in_2d(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawLinesOnTopIn2D

        if temp is None:
            return False

        return temp

    @draw_lines_on_top_in_2d.setter
    @enforce_parameter_types
    def draw_lines_on_top_in_2d(self: Self, value: "bool"):
        self.wrapped.DrawLinesOnTopIn2D = bool(value) if value is not None else False

    @property
    def draw_solid_floor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawSolidFloor

        if temp is None:
            return False

        return temp

    @draw_solid_floor.setter
    @enforce_parameter_types
    def draw_solid_floor(self: Self, value: "bool"):
        self.wrapped.DrawSolidFloor = bool(value) if value is not None else False

    @property
    def flip_axes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.FlipAxes

        if temp is None:
            return False

        return temp

    @flip_axes.setter
    @enforce_parameter_types
    def flip_axes(self: Self, value: "bool"):
        self.wrapped.FlipAxes = bool(value) if value is not None else False

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "WaterfallChartSettings._Cast_WaterfallChartSettings":
        return self._Cast_WaterfallChartSettings(self)
