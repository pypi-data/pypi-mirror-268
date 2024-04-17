"""FlexiblePinAnalysisStopStartAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_STOP_START_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisStopStartAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2812
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisStopStartAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisStopStartAnalysis")


class FlexiblePinAnalysisStopStartAnalysis(_6277.FlexiblePinAnalysis):
    """FlexiblePinAnalysisStopStartAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_STOP_START_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysisStopStartAnalysis")

    class _Cast_FlexiblePinAnalysisStopStartAnalysis:
        """Special nested class for casting FlexiblePinAnalysisStopStartAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis",
            parent: "FlexiblePinAnalysisStopStartAnalysis",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis",
        ) -> "_6277.FlexiblePinAnalysis":
            return self._parent._cast(_6277.FlexiblePinAnalysis)

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis",
        ) -> "_6276.CombinationAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6276,
            )

            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def flexible_pin_analysis_stop_start_analysis(
            self: "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis",
        ) -> "FlexiblePinAnalysisStopStartAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis",
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
        self: Self, instance_to_wrap: "FlexiblePinAnalysisStopStartAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def shaft_extreme_load_case(self: Self) -> "_2812.ShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftExtremeLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_nominal_load_case(self: Self) -> "_2812.ShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftNominalLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis":
        return self._Cast_FlexiblePinAnalysisStopStartAnalysis(self)
