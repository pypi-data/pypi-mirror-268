"""CVTPulleyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CVTPulleyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3809,
        _3850,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyStabilityAnalysis")


class CVTPulleyStabilityAnalysis(_3861.PulleyStabilityAnalysis):
    """CVTPulleyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyStabilityAnalysis")

    class _Cast_CVTPulleyStabilityAnalysis:
        """Special nested class for casting CVTPulleyStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
            parent: "CVTPulleyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_3861.PulleyStabilityAnalysis":
            return self._parent._cast(_3861.PulleyStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_3809.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_3850.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
        ) -> "CVTPulleyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyStabilityAnalysis._Cast_CVTPulleyStabilityAnalysis":
        return self._Cast_CVTPulleyStabilityAnalysis(self)
