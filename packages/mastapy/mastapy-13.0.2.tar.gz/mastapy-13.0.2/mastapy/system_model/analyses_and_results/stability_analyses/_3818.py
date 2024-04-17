"""CycloidalDiscStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CycloidalDiscStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3772,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscStabilityAnalysis")


class CycloidalDiscStabilityAnalysis(_3773.AbstractShaftStabilityAnalysis):
    """CycloidalDiscStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscStabilityAnalysis")

    class _Cast_CycloidalDiscStabilityAnalysis:
        """Special nested class for casting CycloidalDiscStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
            parent: "CycloidalDiscStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3773.AbstractShaftStabilityAnalysis":
            return self._parent._cast(_3773.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3772.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "CycloidalDiscStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis":
        return self._Cast_CycloidalDiscStabilityAnalysis(self)
