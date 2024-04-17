"""TimeSeriesLoadAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "TimeSeriesLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6814
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("TimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="TimeSeriesLoadAnalysisCase")


class TimeSeriesLoadAnalysisCase(_7543.AnalysisCase):
    """TimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeSeriesLoadAnalysisCase")

    class _Cast_TimeSeriesLoadAnalysisCase:
        """Special nested class for casting TimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
            parent: "TimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def analysis_case(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
        ) -> "_7543.AnalysisCase":
            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def multibody_dynamics_analysis(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
        ) -> "_5473.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.MultibodyDynamicsAnalysis)

        @property
        def time_series_load_analysis_case(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
        ) -> "TimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeSeriesLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self: Self) -> "_6814.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase":
        return self._Cast_TimeSeriesLoadAnalysisCase(self)
