"""CompoundAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "CompoundAnalysisCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3097,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5769, _5773
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("CompoundAnalysisCase",)


Self = TypeVar("Self", bound="CompoundAnalysisCase")


class CompoundAnalysisCase(_7558.StaticLoadAnalysisCase):
    """CompoundAnalysisCase

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundAnalysisCase")

    class _Cast_CompoundAnalysisCase:
        """Special nested class for casting CompoundAnalysisCase to subclasses."""

        def __init__(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
            parent: "CompoundAnalysisCase",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def steady_state_synchronous_response(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_3097.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(_3097.SteadyStateSynchronousResponse)

        @property
        def harmonic_analysis(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_5769.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "_7018.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(_7018.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_analysis_case(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase",
        ) -> "CompoundAnalysisCase":
            return self._parent

        def __getattr__(
            self: "CompoundAnalysisCase._Cast_CompoundAnalysisCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CompoundAnalysisCase._Cast_CompoundAnalysisCase":
        return self._Cast_CompoundAnalysisCase(self)
