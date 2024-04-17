"""RingPinsToDiscConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCriticalSpeedAnalysis")


class RingPinsToDiscConnectionCriticalSpeedAnalysis(
    _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """RingPinsToDiscConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
            parent: "RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_6586.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "RingPinsToDiscConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "RingPinsToDiscConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6953.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis":
        return self._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis(self)
