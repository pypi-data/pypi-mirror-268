"""ConceptCouplingConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4077
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ConceptCouplingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.power_flows import _4108, _4075
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionPowerFlow")


class ConceptCouplingConnectionPowerFlow(_4077.CouplingConnectionPowerFlow):
    """ConceptCouplingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingConnectionPowerFlow")

    class _Cast_ConceptCouplingConnectionPowerFlow:
        """Special nested class for casting ConceptCouplingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
            parent: "ConceptCouplingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_power_flow(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_4077.CouplingConnectionPowerFlow":
            return self._parent._cast(_4077.CouplingConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_4108.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_4075.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
        ) -> "ConceptCouplingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2351.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6847.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

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
    ) -> "ConceptCouplingConnectionPowerFlow._Cast_ConceptCouplingConnectionPowerFlow":
        return self._Cast_ConceptCouplingConnectionPowerFlow(self)
