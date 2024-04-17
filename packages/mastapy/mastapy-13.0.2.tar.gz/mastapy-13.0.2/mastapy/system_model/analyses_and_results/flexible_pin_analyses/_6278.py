"""FlexiblePinAnalysisConceptLevel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_CONCEPT_LEVEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisConceptLevel",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2766,
        _2706,
    )
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisConceptLevel",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisConceptLevel")


class FlexiblePinAnalysisConceptLevel(_6277.FlexiblePinAnalysis):
    """FlexiblePinAnalysisConceptLevel

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_CONCEPT_LEVEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysisConceptLevel")

    class _Cast_FlexiblePinAnalysisConceptLevel:
        """Special nested class for casting FlexiblePinAnalysisConceptLevel to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel",
            parent: "FlexiblePinAnalysisConceptLevel",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel",
        ) -> "_6277.FlexiblePinAnalysis":
            return self._parent._cast(_6277.FlexiblePinAnalysis)

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel",
        ) -> "_6276.CombinationAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6276,
            )

            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def flexible_pin_analysis_concept_level(
            self: "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel",
        ) -> "FlexiblePinAnalysisConceptLevel":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAnalysisConceptLevel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flexible_pin_extreme_load_case(
        self: Self,
    ) -> "_2766.FlexiblePinAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinExtremeLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flexible_pin_nominal_load_case(
        self: Self,
    ) -> "_2766.FlexiblePinAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinNominalLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planet_bearings_in_nominal_load(
        self: Self,
    ) -> "List[_2706.BearingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetBearingsInNominalLoad

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel":
        return self._Cast_FlexiblePinAnalysisConceptLevel(self)
