"""CouplingConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4077
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4197,
        _4202,
        _4256,
        _4278,
        _4293,
        _4210,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundPowerFlow")


class CouplingConnectionCompoundPowerFlow(
    _4240.InterMountableComponentConnectionCompoundPowerFlow
):
    """CouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionCompoundPowerFlow")

    class _Cast_CouplingConnectionCompoundPowerFlow:
        """Special nested class for casting CouplingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
            parent: "CouplingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4240.InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4240.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4210.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4197.ClutchConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4202.ConceptCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4256.PartToPartShearCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(
                _4256.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def spring_damper_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4278.SpringDamperConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SpringDamperConnectionCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4293.TorqueConverterConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "CouplingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4077.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4077.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> (
        "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow"
    ):
        return self._Cast_CouplingConnectionCompoundPowerFlow(self)
