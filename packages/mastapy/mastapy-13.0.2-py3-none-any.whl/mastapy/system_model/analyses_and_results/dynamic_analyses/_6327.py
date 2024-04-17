"""CVTPulleyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CVTPulleyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6324,
        _6364,
        _6310,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyDynamicAnalysis")


class CVTPulleyDynamicAnalysis(_6375.PulleyDynamicAnalysis):
    """CVTPulleyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyDynamicAnalysis")

    class _Cast_CVTPulleyDynamicAnalysis:
        """Special nested class for casting CVTPulleyDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
            parent: "CVTPulleyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6375.PulleyDynamicAnalysis":
            return self._parent._cast(_6375.PulleyDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6324.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "CVTPulleyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyDynamicAnalysis.TYPE"):
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
    ) -> "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis":
        return self._Cast_CVTPulleyDynamicAnalysis(self)
