"""AbstractShaftDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6330,
        _6382,
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
__all__ = ("AbstractShaftDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftDynamicAnalysis")


class AbstractShaftDynamicAnalysis(_6287.AbstractShaftOrHousingDynamicAnalysis):
    """AbstractShaftDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftDynamicAnalysis")

    class _Cast_AbstractShaftDynamicAnalysis:
        """Special nested class for casting AbstractShaftDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
            parent: "AbstractShaftDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_6287.AbstractShaftOrHousingDynamicAnalysis":
            return self._parent._cast(_6287.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_6330.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.CycloidalDiscDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "_6382.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.ShaftDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "AbstractShaftDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis":
        return self._Cast_AbstractShaftDynamicAnalysis(self)
