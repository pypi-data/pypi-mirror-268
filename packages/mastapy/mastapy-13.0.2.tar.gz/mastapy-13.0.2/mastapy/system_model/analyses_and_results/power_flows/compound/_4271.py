"""ShaftHubConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ShaftHubConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.power_flows import _4140
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundPowerFlow")


class ShaftHubConnectionCompoundPowerFlow(_4211.ConnectorCompoundPowerFlow):
    """ShaftHubConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionCompoundPowerFlow")

    class _Cast_ShaftHubConnectionCompoundPowerFlow:
        """Special nested class for casting ShaftHubConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
            parent: "ShaftHubConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def connector_compound_power_flow(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_4211.ConnectorCompoundPowerFlow":
            return self._parent._cast(_4211.ConnectorCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
        ) -> "ShaftHubConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4140.ShaftHubConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4140.ShaftHubConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ShaftHubConnectionCompoundPowerFlow._Cast_ShaftHubConnectionCompoundPowerFlow"
    ):
        return self._Cast_ShaftHubConnectionCompoundPowerFlow(self)
