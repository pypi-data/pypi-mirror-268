"""FEPartStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3772
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FEPartStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartStabilityAnalysis",)


Self = TypeVar("Self", bound="FEPartStabilityAnalysis")


class FEPartStabilityAnalysis(_3772.AbstractShaftOrHousingStabilityAnalysis):
    """FEPartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartStabilityAnalysis")

    class _Cast_FEPartStabilityAnalysis:
        """Special nested class for casting FEPartStabilityAnalysis to subclasses."""

        def __init__(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
            parent: "FEPartStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3772.AbstractShaftOrHousingStabilityAnalysis":
            return self._parent._cast(_3772.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "FEPartStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FEPartStabilityAnalysis]

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
    def cast_to(self: Self) -> "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis":
        return self._Cast_FEPartStabilityAnalysis(self)
