"""PartToPartShearCouplingHalfDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PartToPartShearCouplingHalfDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
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
__all__ = ("PartToPartShearCouplingHalfDynamicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfDynamicAnalysis")


class PartToPartShearCouplingHalfDynamicAnalysis(_6324.CouplingHalfDynamicAnalysis):
    """PartToPartShearCouplingHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfDynamicAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfDynamicAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
            parent: "PartToPartShearCouplingHalfDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6324.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6324.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "PartToPartShearCouplingHalfDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis":
        return self._Cast_PartToPartShearCouplingHalfDynamicAnalysis(self)
