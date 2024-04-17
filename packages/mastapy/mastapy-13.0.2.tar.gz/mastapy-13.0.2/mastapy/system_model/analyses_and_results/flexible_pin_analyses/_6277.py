"""FlexiblePinAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
        _6282,
        _6278,
        _6279,
        _6280,
        _6281,
        _6283,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAnalysis")


class FlexiblePinAnalysis(_6276.CombinationAnalysis):
    """FlexiblePinAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysis")

    class _Cast_FlexiblePinAnalysis:
        """Special nested class for casting FlexiblePinAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
            parent: "FlexiblePinAnalysis",
        ):
            self._parent = parent

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6276.CombinationAnalysis":
            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def flexible_pin_analysis_concept_level(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6278.FlexiblePinAnalysisConceptLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6278,
            )

            return self._parent._cast(_6278.FlexiblePinAnalysisConceptLevel)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6279.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6279,
            )

            return self._parent._cast(
                _6279.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
            )

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6280.FlexiblePinAnalysisGearAndBearingRating":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6280,
            )

            return self._parent._cast(_6280.FlexiblePinAnalysisGearAndBearingRating)

        @property
        def flexible_pin_analysis_manufacture_level(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6281.FlexiblePinAnalysisManufactureLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6281,
            )

            return self._parent._cast(_6281.FlexiblePinAnalysisManufactureLevel)

        @property
        def flexible_pin_analysis_stop_start_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6283.FlexiblePinAnalysisStopStartAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6283,
            )

            return self._parent._cast(_6283.FlexiblePinAnalysisStopStartAnalysis)

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "FlexiblePinAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_options(self: Self) -> "_6282.FlexiblePinAnalysisOptions":
        """mastapy.system_model.analyses_and_results.flexible_pin_analyses.FlexiblePinAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis":
        return self._Cast_FlexiblePinAnalysis(self)
