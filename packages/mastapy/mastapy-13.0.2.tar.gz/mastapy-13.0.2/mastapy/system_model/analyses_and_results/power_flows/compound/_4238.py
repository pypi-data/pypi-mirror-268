"""HypoidGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "HypoidGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.power_flows import _4105
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4208,
        _4234,
        _4240,
        _4210,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundPowerFlow")


class HypoidGearMeshCompoundPowerFlow(
    _4180.AGMAGleasonConicalGearMeshCompoundPowerFlow
):
    """HypoidGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshCompoundPowerFlow")

    class _Cast_HypoidGearMeshCompoundPowerFlow:
        """Special nested class for casting HypoidGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
            parent: "HypoidGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_4180.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            return self._parent._cast(_4180.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_4208.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_4234.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(_4234.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_4240.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(
                _4240.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_4210.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
        ) -> "HypoidGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_4105.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

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
    def connection_analysis_cases(self: Self) -> "List[_4105.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

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
    ) -> "HypoidGearMeshCompoundPowerFlow._Cast_HypoidGearMeshCompoundPowerFlow":
        return self._Cast_HypoidGearMeshCompoundPowerFlow(self)
