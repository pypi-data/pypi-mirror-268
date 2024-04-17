"""StabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses", "StabilityAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3880
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysis",)


Self = TypeVar("Self", bound="StabilityAnalysis")


class StabilityAnalysis(_7558.StaticLoadAnalysisCase):
    """StabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysis")

    class _Cast_StabilityAnalysis:
        """Special nested class for casting StabilityAnalysis to subclasses."""

        def __init__(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
            parent: "StabilityAnalysis",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def stability_analysis(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "StabilityAnalysis":
            return self._parent

        def __getattr__(self: "StabilityAnalysis._Cast_StabilityAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stability_analysis_options(self: Self) -> "_3880.StabilityAnalysisOptions":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StabilityAnalysis._Cast_StabilityAnalysis":
        return self._Cast_StabilityAnalysis(self)
