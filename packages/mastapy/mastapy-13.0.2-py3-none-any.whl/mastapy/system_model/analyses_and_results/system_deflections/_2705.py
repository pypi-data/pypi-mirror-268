"""BearingDynamicResultsUIWrapper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_RESULTS_UI_WRAPPER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BearingDynamicResultsUIWrapper",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2706,
        _2704,
        _2702,
        _2703,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingDynamicResultsUIWrapper",)


Self = TypeVar("Self", bound="BearingDynamicResultsUIWrapper")


class BearingDynamicResultsUIWrapper(_0.APIBase):
    """BearingDynamicResultsUIWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_RESULTS_UI_WRAPPER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDynamicResultsUIWrapper")

    class _Cast_BearingDynamicResultsUIWrapper:
        """Special nested class for casting BearingDynamicResultsUIWrapper to subclasses."""

        def __init__(
            self: "BearingDynamicResultsUIWrapper._Cast_BearingDynamicResultsUIWrapper",
            parent: "BearingDynamicResultsUIWrapper",
        ):
            self._parent = parent

        @property
        def bearing_dynamic_results_ui_wrapper(
            self: "BearingDynamicResultsUIWrapper._Cast_BearingDynamicResultsUIWrapper",
        ) -> "BearingDynamicResultsUIWrapper":
            return self._parent

        def __getattr__(
            self: "BearingDynamicResultsUIWrapper._Cast_BearingDynamicResultsUIWrapper",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDynamicResultsUIWrapper.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_revolutions_to_plot(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumRevolutionsToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_revolutions_to_plot.setter
    @enforce_parameter_types
    def maximum_revolutions_to_plot(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumRevolutionsToPlot = value

    @property
    def maximum_time_to_plot(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumTimeToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_time_to_plot.setter
    @enforce_parameter_types
    def maximum_time_to_plot(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumTimeToPlot = value

    @property
    def minimum_revolutions_to_plot(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumRevolutionsToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_revolutions_to_plot.setter
    @enforce_parameter_types
    def minimum_revolutions_to_plot(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumRevolutionsToPlot = value

    @property
    def minimum_time_to_plot(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumTimeToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_time_to_plot.setter
    @enforce_parameter_types
    def minimum_time_to_plot(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumTimeToPlot = value

    @property
    def plot_against_number_of_revolutions(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PlotAgainstNumberOfRevolutions

        if temp is None:
            return False

        return temp

    @plot_against_number_of_revolutions.setter
    @enforce_parameter_types
    def plot_against_number_of_revolutions(self: Self, value: "bool"):
        self.wrapped.PlotAgainstNumberOfRevolutions = (
            bool(value) if value is not None else False
        )

    @property
    def bearing_system_deflection(self: Self) -> "_2706.BearingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_results(
        self: Self,
    ) -> "List[_2704.BearingDynamicResultsPropertyWrapper]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingDynamicResultsPropertyWrapper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cage_results(self: Self) -> "List[_2704.BearingDynamicResultsPropertyWrapper]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingDynamicResultsPropertyWrapper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CageResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def element_results(
        self: Self,
    ) -> "List[_2702.BearingDynamicElementPropertyWrapper]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingDynamicElementPropertyWrapper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def post_analysis_results(
        self: Self,
    ) -> "List[_2703.BearingDynamicPostAnalysisResultWrapper]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingDynamicPostAnalysisResultWrapper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PostAnalysisResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    def clear_all_plots(self: Self):
        """Method does not return."""
        self.wrapped.ClearAllPlots()

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
    def cast_to(
        self: Self,
    ) -> "BearingDynamicResultsUIWrapper._Cast_BearingDynamicResultsUIWrapper":
        return self._Cast_BearingDynamicResultsUIWrapper(self)
