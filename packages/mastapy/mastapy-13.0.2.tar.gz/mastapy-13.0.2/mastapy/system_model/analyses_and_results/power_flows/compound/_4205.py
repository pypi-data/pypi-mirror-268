"""ConceptGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4234
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConceptGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.power_flows import _4069
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4240,
        _4210,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearMeshCompoundPowerFlow")


class ConceptGearMeshCompoundPowerFlow(_4234.GearMeshCompoundPowerFlow):
    """ConceptGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshCompoundPowerFlow")

    class _Cast_ConceptGearMeshCompoundPowerFlow:
        """Special nested class for casting ConceptGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
            parent: "ConceptGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4234.GearMeshCompoundPowerFlow":
            return self._parent._cast(_4234.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4240.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(
                _4240.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4210.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "ConceptGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2312.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2312.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

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
    ) -> "List[_4069.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

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
    def connection_analysis_cases(self: Self) -> "List[_4069.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

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
    ) -> "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow":
        return self._Cast_ConceptGearMeshCompoundPowerFlow(self)
