"""ConceptGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4101
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.concept import _553
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.power_flows import _4108, _4075
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearMeshPowerFlow")


class ConceptGearMeshPowerFlow(_4101.GearMeshPowerFlow):
    """ConceptGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshPowerFlow")

    class _Cast_ConceptGearMeshPowerFlow:
        """Special nested class for casting ConceptGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
            parent: "ConceptGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_power_flow(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_4101.GearMeshPowerFlow":
            return self._parent._cast(_4101.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_4108.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_4075.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow",
        ) -> "ConceptGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_553.ConceptGearMeshRating":
        """mastapy.gears.rating.concept.ConceptGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_553.ConceptGearMeshRating":
        """mastapy.gears.rating.concept.ConceptGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

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
    def connection_load_case(self: Self) -> "_6851.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

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
    ) -> "ConceptGearMeshPowerFlow._Cast_ConceptGearMeshPowerFlow":
        return self._Cast_ConceptGearMeshPowerFlow(self)
