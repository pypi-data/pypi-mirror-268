"""ModalContributionViewOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_CONTRIBUTION_VIEW_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing.Options", "ModalContributionViewOptions"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1496
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
        _5858,
        _5857,
    )
    from mastapy.utility import _1595


__docformat__ = "restructuredtext en"
__all__ = ("ModalContributionViewOptions",)


Self = TypeVar("Self", bound="ModalContributionViewOptions")


class ModalContributionViewOptions(_0.APIBase):
    """ModalContributionViewOptions

    This is a mastapy class.
    """

    TYPE = _MODAL_CONTRIBUTION_VIEW_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalContributionViewOptions")

    class _Cast_ModalContributionViewOptions:
        """Special nested class for casting ModalContributionViewOptions to subclasses."""

        def __init__(
            self: "ModalContributionViewOptions._Cast_ModalContributionViewOptions",
            parent: "ModalContributionViewOptions",
        ):
            self._parent = parent

        @property
        def modal_contribution_view_options(
            self: "ModalContributionViewOptions._Cast_ModalContributionViewOptions",
        ) -> "ModalContributionViewOptions":
            return self._parent

        def __getattr__(
            self: "ModalContributionViewOptions._Cast_ModalContributionViewOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalContributionViewOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def filtering_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilteringFrequency

        if temp is None:
            return 0.0

        return temp

    @filtering_frequency.setter
    @enforce_parameter_types
    def filtering_frequency(self: Self, value: "float"):
        self.wrapped.FilteringFrequency = float(value) if value is not None else 0.0

    @property
    def filtering_frequency_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.FilteringFrequencyRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @filtering_frequency_range.setter
    @enforce_parameter_types
    def filtering_frequency_range(self: Self, value: "_1496.Range"):
        self.wrapped.FilteringFrequencyRange = value.wrapped

    @property
    def filtering_method(self: Self) -> "_5858.ModalContributionFilteringMethod":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ModalContributionFilteringMethod"""
        temp = self.wrapped.FilteringMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionFilteringMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.harmonic_analyses.results._5858",
            "ModalContributionFilteringMethod",
        )(value)

    @filtering_method.setter
    @enforce_parameter_types
    def filtering_method(self: Self, value: "_5858.ModalContributionFilteringMethod"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionFilteringMethod",
        )
        self.wrapped.FilteringMethod = value

    @property
    def frequency_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.FrequencyRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @frequency_range.setter
    @enforce_parameter_types
    def frequency_range(self: Self, value: "_1496.Range"):
        self.wrapped.FrequencyRange = value.wrapped

    @property
    def index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Index

        if temp is None:
            return 0

        return temp

    @index.setter
    @enforce_parameter_types
    def index(self: Self, value: "int"):
        self.wrapped.Index = int(value) if value is not None else 0

    @property
    def index_range(self: Self) -> "_1595.IntegerRange":
        """mastapy.utility.IntegerRange"""
        temp = self.wrapped.IndexRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @index_range.setter
    @enforce_parameter_types
    def index_range(self: Self, value: "_1595.IntegerRange"):
        self.wrapped.IndexRange = value.wrapped

    @property
    def modes_to_display(self: Self) -> "_5857.ModalContributionDisplayMethod":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ModalContributionDisplayMethod"""
        temp = self.wrapped.ModesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionDisplayMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.harmonic_analyses.results._5857",
            "ModalContributionDisplayMethod",
        )(value)

    @modes_to_display.setter
    @enforce_parameter_types
    def modes_to_display(self: Self, value: "_5857.ModalContributionDisplayMethod"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionDisplayMethod",
        )
        self.wrapped.ModesToDisplay = value

    @property
    def percentage_of_total_response(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageOfTotalResponse

        if temp is None:
            return 0.0

        return temp

    @percentage_of_total_response.setter
    @enforce_parameter_types
    def percentage_of_total_response(self: Self, value: "float"):
        self.wrapped.PercentageOfTotalResponse = (
            float(value) if value is not None else 0.0
        )

    @property
    def show_modal_contribution(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowModalContribution

        if temp is None:
            return False

        return temp

    @show_modal_contribution.setter
    @enforce_parameter_types
    def show_modal_contribution(self: Self, value: "bool"):
        self.wrapped.ShowModalContribution = bool(value) if value is not None else False

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
    def cast_to(
        self: Self,
    ) -> "ModalContributionViewOptions._Cast_ModalContributionViewOptions":
        return self._Cast_ModalContributionViewOptions(self)
