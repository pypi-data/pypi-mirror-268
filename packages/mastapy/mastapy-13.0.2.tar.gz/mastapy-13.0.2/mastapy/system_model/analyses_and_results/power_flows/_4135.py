"""RingPinsToDiscConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4108
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "RingPinsToDiscConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.power_flows import _4075
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionPowerFlow",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionPowerFlow")


class RingPinsToDiscConnectionPowerFlow(
    _4108.InterMountableComponentConnectionPowerFlow
):
    """RingPinsToDiscConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsToDiscConnectionPowerFlow")

    class _Cast_RingPinsToDiscConnectionPowerFlow:
        """Special nested class for casting RingPinsToDiscConnectionPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
            parent: "RingPinsToDiscConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_4108.InterMountableComponentConnectionPowerFlow":
            return self._parent._cast(_4108.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_4075.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "RingPinsToDiscConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionPowerFlow.TYPE"
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
    ) -> "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow":
        return self._Cast_RingPinsToDiscConnectionPowerFlow(self)
