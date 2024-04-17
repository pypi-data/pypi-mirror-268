"""FrequencyOptionsForHarmonicAnalysisResults"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCY_OPTIONS_FOR_HARMONIC_ANALYSIS_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "FrequencyOptionsForHarmonicAnalysisResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("FrequencyOptionsForHarmonicAnalysisResults",)


Self = TypeVar("Self", bound="FrequencyOptionsForHarmonicAnalysisResults")


class FrequencyOptionsForHarmonicAnalysisResults(
    _7544.AbstractAnalysisOptions["_6813.StaticLoadCase"]
):
    """FrequencyOptionsForHarmonicAnalysisResults

    This is a mastapy class.
    """

    TYPE = _FREQUENCY_OPTIONS_FOR_HARMONIC_ANALYSIS_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FrequencyOptionsForHarmonicAnalysisResults"
    )

    class _Cast_FrequencyOptionsForHarmonicAnalysisResults:
        """Special nested class for casting FrequencyOptionsForHarmonicAnalysisResults to subclasses."""

        def __init__(
            self: "FrequencyOptionsForHarmonicAnalysisResults._Cast_FrequencyOptionsForHarmonicAnalysisResults",
            parent: "FrequencyOptionsForHarmonicAnalysisResults",
        ):
            self._parent = parent

        @property
        def abstract_analysis_options(
            self: "FrequencyOptionsForHarmonicAnalysisResults._Cast_FrequencyOptionsForHarmonicAnalysisResults",
        ) -> "_7544.AbstractAnalysisOptions":
            return self._parent._cast(_7544.AbstractAnalysisOptions)

        @property
        def frequency_options_for_harmonic_analysis_results(
            self: "FrequencyOptionsForHarmonicAnalysisResults._Cast_FrequencyOptionsForHarmonicAnalysisResults",
        ) -> "FrequencyOptionsForHarmonicAnalysisResults":
            return self._parent

        def __getattr__(
            self: "FrequencyOptionsForHarmonicAnalysisResults._Cast_FrequencyOptionsForHarmonicAnalysisResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "FrequencyOptionsForHarmonicAnalysisResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_maximum_above_highest_mode(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.AllowMaximumAboveHighestMode

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @allow_maximum_above_highest_mode.setter
    @enforce_parameter_types
    def allow_maximum_above_highest_mode(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.AllowMaximumAboveHighestMode = value

    @property
    def base_points_on_mode_frequencies(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.BasePointsOnModeFrequencies

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @base_points_on_mode_frequencies.setter
    @enforce_parameter_types
    def base_points_on_mode_frequencies(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.BasePointsOnModeFrequencies = value

    @property
    def clustering_bias_of_additional_points(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ClusteringBiasOfAdditionalPoints

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @clustering_bias_of_additional_points.setter
    @enforce_parameter_types
    def clustering_bias_of_additional_points(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ClusteringBiasOfAdditionalPoints = value

    @property
    def logarithmic_frequency_axis(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.LogarithmicFrequencyAxis

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @logarithmic_frequency_axis.setter
    @enforce_parameter_types
    def logarithmic_frequency_axis(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.LogarithmicFrequencyAxis = value

    @property
    def maximum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum.setter
    @enforce_parameter_types
    def maximum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Maximum = value

    @property
    def minimum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum.setter
    @enforce_parameter_types
    def minimum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Minimum = value

    @property
    def number_of_points_across_range(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsAcrossRange

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_across_range.setter
    @enforce_parameter_types
    def number_of_points_across_range(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsAcrossRange = value

    @property
    def number_of_points_per_step_for_torque_map(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsPerStepForTorqueMap

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_per_step_for_torque_map.setter
    @enforce_parameter_types
    def number_of_points_per_step_for_torque_map(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsPerStepForTorqueMap = value

    @property
    def use_logarithmic_spacing(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseLogarithmicSpacing

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_logarithmic_spacing.setter
    @enforce_parameter_types
    def use_logarithmic_spacing(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseLogarithmicSpacing = value

    @property
    def design_defaults(self: Self) -> "FrequencyOptionsForHarmonicAnalysisResults":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FrequencyOptionsForHarmonicAnalysisResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "FrequencyOptionsForHarmonicAnalysisResults._Cast_FrequencyOptionsForHarmonicAnalysisResults":
        return self._Cast_FrequencyOptionsForHarmonicAnalysisResults(self)
