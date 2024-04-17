"""AdvancedTimeSteppingAnalysisForModulationOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6821, _6904
    from mastapy.system_model.analyses_and_results import _2692


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedTimeSteppingAnalysisForModulationOptions",)


Self = TypeVar("Self", bound="AdvancedTimeSteppingAnalysisForModulationOptions")


class AdvancedTimeSteppingAnalysisForModulationOptions(_0.APIBase):
    """AdvancedTimeSteppingAnalysisForModulationOptions

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AdvancedTimeSteppingAnalysisForModulationOptions"
    )

    class _Cast_AdvancedTimeSteppingAnalysisForModulationOptions:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulationOptions to subclasses."""

        def __init__(
            self: "AdvancedTimeSteppingAnalysisForModulationOptions._Cast_AdvancedTimeSteppingAnalysisForModulationOptions",
            parent: "AdvancedTimeSteppingAnalysisForModulationOptions",
        ):
            self._parent = parent

        @property
        def advanced_time_stepping_analysis_for_modulation_options(
            self: "AdvancedTimeSteppingAnalysisForModulationOptions._Cast_AdvancedTimeSteppingAnalysisForModulationOptions",
        ) -> "AdvancedTimeSteppingAnalysisForModulationOptions":
            return self._parent

        def __getattr__(
            self: "AdvancedTimeSteppingAnalysisForModulationOptions._Cast_AdvancedTimeSteppingAnalysisForModulationOptions",
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
        self: Self,
        instance_to_wrap: "AdvancedTimeSteppingAnalysisForModulationOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_method(
        self: Self,
    ) -> "_6821.AdvancedTimeSteppingAnalysisForModulationType":
        """mastapy.system_model.analyses_and_results.static_loads.AdvancedTimeSteppingAnalysisForModulationType"""
        temp = self.wrapped.AdvancedTimeSteppingAnalysisMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AdvancedTimeSteppingAnalysisForModulationType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6821",
            "AdvancedTimeSteppingAnalysisForModulationType",
        )(value)

    @advanced_time_stepping_analysis_method.setter
    @enforce_parameter_types
    def advanced_time_stepping_analysis_method(
        self: Self, value: "_6821.AdvancedTimeSteppingAnalysisForModulationType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AdvancedTimeSteppingAnalysisForModulationType",
        )
        self.wrapped.AdvancedTimeSteppingAnalysisMethod = value

    @property
    def include_time_offset_for_steady_state(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTimeOffsetForSteadyState

        if temp is None:
            return False

        return temp

    @include_time_offset_for_steady_state.setter
    @enforce_parameter_types
    def include_time_offset_for_steady_state(self: Self, value: "bool"):
        self.wrapped.IncludeTimeOffsetForSteadyState = (
            bool(value) if value is not None else False
        )

    @property
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = (
            self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts
        )

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    @enforce_parameter_types
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(
        self: Self, value: "_6813.StaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = (
            value
        )

    @property
    def number_of_periods_for_advanced_time_stepping_analysis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis

        if temp is None:
            return 0.0

        return temp

    @number_of_periods_for_advanced_time_stepping_analysis.setter
    @enforce_parameter_types
    def number_of_periods_for_advanced_time_stepping_analysis(
        self: Self, value: "float"
    ):
        self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_steps_for_advanced_time_stepping_analysis(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_advanced_time_stepping_analysis.setter
    @enforce_parameter_types
    def number_of_steps_for_advanced_time_stepping_analysis(self: Self, value: "int"):
        self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_times_per_quasi_step(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTimesPerQuasiStep

        if temp is None:
            return 0

        return temp

    @number_of_times_per_quasi_step.setter
    @enforce_parameter_types
    def number_of_times_per_quasi_step(self: Self, value: "int"):
        self.wrapped.NumberOfTimesPerQuasiStep = int(value) if value is not None else 0

    @property
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_compatibility_of_atsam_and_te_periods_check.setter
    @enforce_parameter_types
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(
        self: Self, value: "float"
    ):
        self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    @enforce_parameter_types
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(
        self: Self, value: "bool"
    ):
        self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = (
            bool(value) if value is not None else False
        )

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "_6904.GearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_options(self: Self) -> "_2692.TimeOptions":
        """mastapy.system_model.analyses_and_results.TimeOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedTimeSteppingAnalysisForModulationOptions._Cast_AdvancedTimeSteppingAnalysisForModulationOptions":
        return self._Cast_AdvancedTimeSteppingAnalysisForModulationOptions(self)
