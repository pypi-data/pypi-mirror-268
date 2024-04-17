"""DynamicModelForHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "DynamicModelForHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7552,
        _7558,
        _7543,
    )
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForHarmonicAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForHarmonicAnalysis")


class DynamicModelForHarmonicAnalysis(_6337.DynamicAnalysis):
    """DynamicModelForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForHarmonicAnalysis")

    class _Cast_DynamicModelForHarmonicAnalysis:
        """Special nested class for casting DynamicModelForHarmonicAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
            parent: "DynamicModelForHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "_6337.DynamicAnalysis":
            return self._parent._cast(_6337.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "_7552.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7552

            return self._parent._cast(_7552.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
        ) -> "DynamicModelForHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis":
        return self._Cast_DynamicModelForHarmonicAnalysis(self)
