"""RollingRingConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "RollingRingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionDynamicAnalysis")


class RollingRingConnectionDynamicAnalysis(
    _6352.InterMountableComponentConnectionDynamicAnalysis
):
    """RollingRingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingConnectionDynamicAnalysis")

    class _Cast_RollingRingConnectionDynamicAnalysis:
        """Special nested class for casting RollingRingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
            parent: "RollingRingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_6352.InterMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6352.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
        ) -> "RollingRingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6955.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingConnectionDynamicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionDynamicAnalysis._Cast_RollingRingConnectionDynamicAnalysis":
        return self._Cast_RollingRingConnectionDynamicAnalysis(self)
