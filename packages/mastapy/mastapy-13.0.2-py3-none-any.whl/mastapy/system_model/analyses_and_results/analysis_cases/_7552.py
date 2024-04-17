"""FEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "FEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2833,
        _2840,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3043,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import _3824
    from mastapy.system_model.analyses_and_results.modal_analyses import _4633
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4917,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7284,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("FEAnalysis",)


Self = TypeVar("Self", bound="FEAnalysis")


class FEAnalysis(_7558.StaticLoadAnalysisCase):
    """FEAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEAnalysis")

    class _Cast_FEAnalysis:
        """Special nested class for casting FEAnalysis to subclasses."""

        def __init__(self: "FEAnalysis._Cast_FEAnalysis", parent: "FEAnalysis"):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(self: "FEAnalysis._Cast_FEAnalysis") -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(self: "FEAnalysis._Cast_FEAnalysis") -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def system_deflection(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_2833.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_2840.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_3043.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(
                _3043.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def dynamic_model_for_stability_analysis(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_3824.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_modal_analysis(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_4633.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_4917.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.DynamicModelAtAStiffness)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_5740.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_6337.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.DynamicAnalysis)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "FEAnalysis._Cast_FEAnalysis",
        ) -> "_7284.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(_7284.AdvancedSystemDeflectionSubAnalysis)

        @property
        def fe_analysis(self: "FEAnalysis._Cast_FEAnalysis") -> "FEAnalysis":
            return self._parent

        def __getattr__(self: "FEAnalysis._Cast_FEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_with_respect_to_input_power_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessWithRespectToInputPowerLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_at_zero_displacement_for_input_power_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueAtZeroDisplacementForInputPowerLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_to_output(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioToOutput

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "FEAnalysis._Cast_FEAnalysis":
        return self._Cast_FEAnalysis(self)
