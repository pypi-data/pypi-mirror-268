"""ConnectorCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConnectorCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6559,
        _6632,
        _6650,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectorCriticalSpeedAnalysis")


class ConnectorCriticalSpeedAnalysis(_6631.MountableComponentCriticalSpeedAnalysis):
    """ConnectorCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCriticalSpeedAnalysis")

    class _Cast_ConnectorCriticalSpeedAnalysis:
        """Special nested class for casting ConnectorCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
            parent: "ConnectorCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6559.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(_6559.BearingCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6632.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.OilSealCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6650.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "ConnectorCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCriticalSpeedAnalysis.TYPE"):
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
    ) -> "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis":
        return self._Cast_ConnectorCriticalSpeedAnalysis(self)
