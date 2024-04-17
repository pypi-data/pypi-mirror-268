"""BevelGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6563,
        _6654,
        _6660,
        _6663,
        _6681,
        _6584,
        _6613,
        _6619,
        _6586,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCriticalSpeedAnalysis")


class BevelGearMeshCriticalSpeedAnalysis(
    _6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
):
    """BevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCriticalSpeedAnalysis")

    class _Cast_BevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
            parent: "BevelGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(
                _6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6584.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(_6613.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6586.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6563.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(
                _6563.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6654.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(
                _6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6663.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6681.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6681,
            )

            return self._parent._cast(_6681.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "BevelGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2310.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis":
        return self._Cast_BevelGearMeshCriticalSpeedAnalysis(self)
