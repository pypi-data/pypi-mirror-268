"""FlexiblePinAnalysisGearAndBearingRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_GEAR_AND_BEARING_RATING = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisGearAndBearingRating",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2908,
        _2867,
    )
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisGearAndBearingRating",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisGearAndBearingRating")


class FlexiblePinAnalysisGearAndBearingRating(_6277.FlexiblePinAnalysis):
    """FlexiblePinAnalysisGearAndBearingRating

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_GEAR_AND_BEARING_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAnalysisGearAndBearingRating"
    )

    class _Cast_FlexiblePinAnalysisGearAndBearingRating:
        """Special nested class for casting FlexiblePinAnalysisGearAndBearingRating to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating",
            parent: "FlexiblePinAnalysisGearAndBearingRating",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating",
        ) -> "_6277.FlexiblePinAnalysis":
            return self._parent._cast(_6277.FlexiblePinAnalysis)

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating",
        ) -> "_6276.CombinationAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6276,
            )

            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(
            self: "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating",
        ) -> "FlexiblePinAnalysisGearAndBearingRating":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating",
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
        self: Self, instance_to_wrap: "FlexiblePinAnalysisGearAndBearingRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_analysis(
        self: Self,
    ) -> "_2908.CylindricalGearSetCompoundSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearSetCompoundSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_analyses(self: Self) -> "List[_2867.BearingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.BearingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating":
        return self._Cast_FlexiblePinAnalysisGearAndBearingRating(self)
