"""ConicalGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2314
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6556,
        _6563,
        _6568,
        _6617,
        _6621,
        _6624,
        _6627,
        _6654,
        _6660,
        _6663,
        _6681,
        _6619,
        _6586,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCriticalSpeedAnalysis")


class ConicalGearMeshCriticalSpeedAnalysis(_6613.GearMeshCriticalSpeedAnalysis):
    """ConicalGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshCriticalSpeedAnalysis")

    class _Cast_ConicalGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
            parent: "ConicalGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.GearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6613.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6586.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6563.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(
                _6563.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6568.BevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6617.HypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6621.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(
                _6621.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(
                _6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6654.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(
                _6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6663.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6681.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6681,
            )

            return self._parent._cast(_6681.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "ConicalGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2314.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis":
        return self._Cast_ConicalGearMeshCriticalSpeedAnalysis(self)
