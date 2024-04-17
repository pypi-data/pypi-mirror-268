"""RingPinsToDiscConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "RingPinsToDiscConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundPowerFlow")


class RingPinsToDiscConnectionCompoundPowerFlow(
    _4240.InterMountableComponentConnectionCompoundPowerFlow
):
    """RingPinsToDiscConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCompoundPowerFlow"
    )

    class _Cast_RingPinsToDiscConnectionCompoundPowerFlow:
        """Special nested class for casting RingPinsToDiscConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
            parent: "RingPinsToDiscConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "_4240.InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4240.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "_4210.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
        ) -> "RingPinsToDiscConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4135.RingPinsToDiscConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RingPinsToDiscConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4135.RingPinsToDiscConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RingPinsToDiscConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCompoundPowerFlow._Cast_RingPinsToDiscConnectionCompoundPowerFlow":
        return self._Cast_RingPinsToDiscConnectionCompoundPowerFlow(self)
