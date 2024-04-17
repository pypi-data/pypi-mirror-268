"""ConnectorDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConnectorDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6293,
        _6365,
        _6383,
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
__all__ = ("ConnectorDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectorDynamicAnalysis")


class ConnectorDynamicAnalysis(_6364.MountableComponentDynamicAnalysis):
    """ConnectorDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorDynamicAnalysis")

    class _Cast_ConnectorDynamicAnalysis:
        """Special nested class for casting ConnectorDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
            parent: "ConnectorDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6293.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BearingDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6365.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.OilSealDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "_6383.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.ShaftHubConnectionDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "ConnectorDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis":
        return self._Cast_ConnectorDynamicAnalysis(self)
