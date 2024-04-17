"""ShaftStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ShaftStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3811,
        _3772,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftStabilityAnalysis",)


Self = TypeVar("Self", bound="ShaftStabilityAnalysis")


class ShaftStabilityAnalysis(_3773.AbstractShaftStabilityAnalysis):
    """ShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftStabilityAnalysis")

    class _Cast_ShaftStabilityAnalysis:
        """Special nested class for casting ShaftStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
            parent: "ShaftStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3773.AbstractShaftStabilityAnalysis":
            return self._parent._cast(_3773.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3772.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "ShaftStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6959.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speeds(self: Self) -> "List[_3811.CriticalSpeed]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CriticalSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeeds

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[ShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis":
        return self._Cast_ShaftStabilityAnalysis(self)
