"""FaceGearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6742,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6608
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6748,
        _6718,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshCompoundCriticalSpeedAnalysis")


class FaceGearMeshCompoundCriticalSpeedAnalysis(
    _6742.GearMeshCompoundCriticalSpeedAnalysis
):
    """FaceGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_FaceGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FaceGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
            parent: "FaceGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6742.GearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6742.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "FaceGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2318.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2318.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

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
    ) -> "List[_6608.FaceGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FaceGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6608.FaceGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FaceGearMeshCriticalSpeedAnalysis]

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
    ) -> "FaceGearMeshCompoundCriticalSpeedAnalysis._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_FaceGearMeshCompoundCriticalSpeedAnalysis(self)
