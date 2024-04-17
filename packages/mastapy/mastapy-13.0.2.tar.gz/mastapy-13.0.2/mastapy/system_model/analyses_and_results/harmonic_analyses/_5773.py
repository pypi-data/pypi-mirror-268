"""HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
        "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7545,
        _7558,
        _7543,
    )
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
)


class HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
    _5769.HarmonicAnalysis
):
    """HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
            parent: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def harmonic_analysis(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_5769.HarmonicAnalysis":
            return self._parent._cast(_5769.HarmonicAnalysis)

        @property
        def compound_analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
            self
        )
