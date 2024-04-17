"""StaticLoadAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "StaticLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6813
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
    from mastapy.system_model.analyses_and_results.modal_analyses import _4633, _4662
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4917,
        _4943,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5202,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5740,
        _5769,
        _5773,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6078,
        _6094,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7282,
        _7284,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7552
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("StaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="StaticLoadAnalysisCase")


class StaticLoadAnalysisCase(_7543.AnalysisCase):
    """StaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticLoadAnalysisCase")

    class _Cast_StaticLoadAnalysisCase:
        """Special nested class for casting StaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
            parent: "StaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7543.AnalysisCase":
            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2833.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2840.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3043.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(
                _3043.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3097.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(_3097.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3358.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(_3358.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3617.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(_3617.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3824.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3878.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StabilityAnalysis)

        @property
        def power_flow(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4130.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.PowerFlow)

        @property
        def dynamic_model_for_modal_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4633.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4662.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4917.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4943.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5202.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.ModalAnalysisAtASpeed)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5740.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5769.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6078.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(_6078.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6094.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6337.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6591.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7018.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(_7018.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7282.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(_7282.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7284.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(_7284.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7545.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.CompoundAnalysisCase)

        @property
        def fe_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7552.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7552

            return self._parent._cast(_7552.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "StaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase":
        return self._Cast_StaticLoadAnalysisCase(self)
