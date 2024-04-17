"""Context"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTEXT = python_net_import("SMT.MastaAPI.SystemModel.AnalysesAndResults", "Context")

if TYPE_CHECKING:
    from mastapy.utility import _1590
    from mastapy.system_model import _2207
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2833,
        _2840,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3043,
        _3097,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3358,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3617,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3824,
        _3878,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4130
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4395,
        _4396,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4633, _4662
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4917,
        _4943,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5202,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5740,
        _5769,
        _5773,
        _5778,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6078,
        _6094,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6812,
        _6813,
        _6814,
        _6820,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7282,
        _7284,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7543,
        _7545,
        _7552,
        _7558,
        _7559,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Context",)


Self = TypeVar("Self", bound="Context")


class Context(_0.APIBase):
    """Context

    This is a mastapy class.
    """

    TYPE = _CONTEXT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Context")

    class _Cast_Context:
        """Special nested class for casting Context to subclasses."""

        def __init__(self: "Context._Cast_Context", parent: "Context"):
            self._parent = parent

        @property
        def system_deflection(
            self: "Context._Cast_Context",
        ) -> "_2833.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "Context._Cast_Context",
        ) -> "_2840.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "Context._Cast_Context",
        ) -> "_3043.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(
                _3043.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "Context._Cast_Context",
        ) -> "_3097.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(_3097.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "Context._Cast_Context",
        ) -> "_3358.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(_3358.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "Context._Cast_Context",
        ) -> "_3617.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(_3617.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "Context._Cast_Context",
        ) -> "_3824.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "Context._Cast_Context",
        ) -> "_3878.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StabilityAnalysis)

        @property
        def power_flow(self: "Context._Cast_Context") -> "_4130.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.PowerFlow)

        @property
        def parametric_study_static_load(
            self: "Context._Cast_Context",
        ) -> "_4395.ParametricStudyStaticLoad":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.ParametricStudyStaticLoad)

        @property
        def parametric_study_tool(
            self: "Context._Cast_Context",
        ) -> "_4396.ParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(
            self: "Context._Cast_Context",
        ) -> "_4633.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "Context._Cast_Context") -> "_4662.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "Context._Cast_Context",
        ) -> "_4917.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "Context._Cast_Context",
        ) -> "_4943.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "Context._Cast_Context",
        ) -> "_5202.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(
            self: "Context._Cast_Context",
        ) -> "_5473.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_5740.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_5769.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ) -> "_5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "Context._Cast_Context",
        ) -> "_5778.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "Context._Cast_Context",
        ) -> "_6078.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(_6078.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_6094.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self: "Context._Cast_Context") -> "_6337.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "Context._Cast_Context",
        ) -> "_6591.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CriticalSpeedAnalysis)

        @property
        def load_case(self: "Context._Cast_Context") -> "_6812.LoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.LoadCase)

        @property
        def static_load_case(self: "Context._Cast_Context") -> "_6813.StaticLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.StaticLoadCase)

        @property
        def time_series_load_case(
            self: "Context._Cast_Context",
        ) -> "_6814.TimeSeriesLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6814

            return self._parent._cast(_6814.TimeSeriesLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "Context._Cast_Context",
        ) -> "_6820.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(
                _6820.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
            )

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ) -> "_7018.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(_7018.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "Context._Cast_Context",
        ) -> "_7282.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(_7282.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "Context._Cast_Context",
        ) -> "_7284.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(_7284.AdvancedSystemDeflectionSubAnalysis)

        @property
        def analysis_case(self: "Context._Cast_Context") -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def compound_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7545.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "Context._Cast_Context") -> "_7552.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7552

            return self._parent._cast(_7552.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7559.TimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.TimeSeriesLoadAnalysisCase)

        @property
        def context(self: "Context._Cast_Context") -> "Context":
            return self._parent

        def __getattr__(self: "Context._Cast_Context", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Context.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def save_history_information(self: Self) -> "_1590.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SaveHistoryInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_properties(self: Self) -> "_2207.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

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
    def cast_to(self: Self) -> "Context._Cast_Context":
        return self._Cast_Context(self)
