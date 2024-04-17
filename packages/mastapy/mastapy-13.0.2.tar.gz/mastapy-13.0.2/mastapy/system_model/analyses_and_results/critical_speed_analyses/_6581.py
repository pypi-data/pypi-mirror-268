"""ConceptGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConceptGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6619,
        _6586,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearMeshCriticalSpeedAnalysis")


class ConceptGearMeshCriticalSpeedAnalysis(_6613.GearMeshCriticalSpeedAnalysis):
    """ConceptGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshCriticalSpeedAnalysis")

    class _Cast_ConceptGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
            parent: "ConceptGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.GearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6613.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_6586.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
        ) -> "ConceptGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "ConceptGearMeshCriticalSpeedAnalysis._Cast_ConceptGearMeshCriticalSpeedAnalysis":
        return self._Cast_ConceptGearMeshCriticalSpeedAnalysis(self)
