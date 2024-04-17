"""SynchroniserSleeveDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserSleeveDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.static_loads import _6979
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
__all__ = ("SynchroniserSleeveDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveDynamicAnalysis")


class SynchroniserSleeveDynamicAnalysis(_6402.SynchroniserPartDynamicAnalysis):
    """SynchroniserSleeveDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveDynamicAnalysis")

    class _Cast_SynchroniserSleeveDynamicAnalysis:
        """Special nested class for casting SynchroniserSleeveDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
            parent: "SynchroniserSleeveDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_6402.SynchroniserPartDynamicAnalysis":
            return self._parent._cast(_6402.SynchroniserPartDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_6324.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "SynchroniserSleeveDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6979.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis":
        return self._Cast_SynchroniserSleeveDynamicAnalysis(self)
