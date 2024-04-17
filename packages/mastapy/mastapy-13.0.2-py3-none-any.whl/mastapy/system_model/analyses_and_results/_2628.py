"""SingleAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy import _7561
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")
_DESIGN_ENTITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "DesignEntityAnalysis"
)
_SINGLE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "SingleAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7567
    from mastapy.system_model import _2210
    from mastapy.system_model.analyses_and_results import (
        _2659,
        _2629,
        _2630,
        _2631,
        _2632,
        _2633,
        _2634,
        _2635,
        _2636,
        _2637,
        _2638,
        _2639,
        _2640,
        _2641,
        _2642,
        _2643,
        _2644,
        _2645,
        _2646,
        _2647,
        _2648,
        _2649,
        _2650,
        _2651,
        _2652,
        _2653,
        _2654,
        _2655,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SingleAnalysis",)


Self = TypeVar("Self", bound="SingleAnalysis")


class SingleAnalysis(_7561.MarshalByRefObjectPermanent):
    """SingleAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingleAnalysis")

    class _Cast_SingleAnalysis:
        """Special nested class for casting SingleAnalysis to subclasses."""

        def __init__(
            self: "SingleAnalysis._Cast_SingleAnalysis", parent: "SingleAnalysis"
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def advanced_system_deflection_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2629.AdvancedSystemDeflectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2629

            return self._parent._cast(_2629.AdvancedSystemDeflectionAnalysis)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2630.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results import _2630

            return self._parent._cast(_2630.AdvancedSystemDeflectionSubAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2631.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results import _2631

            return self._parent._cast(_2631.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_parametric_study_tool_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2632.CompoundParametricStudyToolAnalysis":
            from mastapy.system_model.analyses_and_results import _2632

            return self._parent._cast(_2632.CompoundParametricStudyToolAnalysis)

        @property
        def critical_speed_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2633.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results import _2633

            return self._parent._cast(_2633.CriticalSpeedAnalysis)

        @property
        def dynamic_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2634.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results import _2634

            return self._parent._cast(_2634.DynamicAnalysis)

        @property
        def dynamic_model_at_a_stiffness_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2635.DynamicModelAtAStiffnessAnalysis":
            from mastapy.system_model.analyses_and_results import _2635

            return self._parent._cast(_2635.DynamicModelAtAStiffnessAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2636.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results import _2636

            return self._parent._cast(_2636.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_model_for_modal_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2637.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results import _2637

            return self._parent._cast(_2637.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_for_stability_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2638.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results import _2638

            return self._parent._cast(_2638.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_steady_state_synchronous_response_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2639.DynamicModelForSteadyStateSynchronousResponseAnalysis":
            from mastapy.system_model.analyses_and_results import _2639

            return self._parent._cast(
                _2639.DynamicModelForSteadyStateSynchronousResponseAnalysis
            )

        @property
        def harmonic_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2640.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results import _2640

            return self._parent._cast(_2640.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2641.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results import _2641

            return self._parent._cast(
                _2641.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2642.HarmonicAnalysisOfSingleExcitationAnalysis":
            from mastapy.system_model.analyses_and_results import _2642

            return self._parent._cast(_2642.HarmonicAnalysisOfSingleExcitationAnalysis)

        @property
        def modal_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2643.ModalAnalysis":
            from mastapy.system_model.analyses_and_results import _2643

            return self._parent._cast(_2643.ModalAnalysis)

        @property
        def modal_analysis_at_a_speed(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2644.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results import _2644

            return self._parent._cast(_2644.ModalAnalysisAtASpeed)

        @property
        def modal_analysis_at_a_stiffness(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2645.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results import _2645

            return self._parent._cast(_2645.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2646.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ModalAnalysisForHarmonicAnalysis)

        @property
        def multibody_dynamics_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2647.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.MultibodyDynamicsAnalysis)

        @property
        def parametric_study_tool_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2648.ParametricStudyToolAnalysis":
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.ParametricStudyToolAnalysis)

        @property
        def power_flow_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2649.PowerFlowAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.PowerFlowAnalysis)

        @property
        def stability_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2650.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.StabilityAnalysis)

        @property
        def steady_state_synchronous_response_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2651.SteadyStateSynchronousResponseAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.SteadyStateSynchronousResponseAnalysis)

        @property
        def steady_state_synchronous_response_at_a_speed_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2652.SteadyStateSynchronousResponseAtASpeedAnalysis":
            from mastapy.system_model.analyses_and_results import _2652

            return self._parent._cast(
                _2652.SteadyStateSynchronousResponseAtASpeedAnalysis
            )

        @property
        def steady_state_synchronous_response_on_a_shaft_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2653.SteadyStateSynchronousResponseOnAShaftAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(
                _2653.SteadyStateSynchronousResponseOnAShaftAnalysis
            )

        @property
        def system_deflection_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2654.SystemDeflectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.SystemDeflectionAnalysis)

        @property
        def torsional_system_deflection_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "_2655.TorsionalSystemDeflectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.TorsionalSystemDeflectionAnalysis)

        @property
        def single_analysis(
            self: "SingleAnalysis._Cast_SingleAnalysis",
        ) -> "SingleAnalysis":
            return self._parent

        def __getattr__(self: "SingleAnalysis._Cast_SingleAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingleAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @enforce_parameter_types
    def perform_analysis_with_progress(self: Self, task_progress: "_7567.TaskProgress"):
        """Method does not return.

        Args:
            task_progress (mastapy.TaskProgress)
        """
        self.wrapped.PerformAnalysis.Overloads[_TASK_PROGRESS](
            task_progress.wrapped if task_progress else None
        )

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2210.DesignEntity"
    ) -> "_2659.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DESIGN_ENTITY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_design_entity_analysis(
        self: Self, design_entity_analysis: "_2659.DesignEntityAnalysis"
    ) -> "_2659.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.DesignEntityAnalysis)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DESIGN_ENTITY_ANALYSIS](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "SingleAnalysis._Cast_SingleAnalysis":
        return self._Cast_SingleAnalysis(self)
