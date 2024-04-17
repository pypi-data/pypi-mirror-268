"""BevelGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5397,
        _5498,
        _5504,
        _5507,
        _5528,
        _5419,
        _5445,
        _5457,
        _5422,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshMultibodyDynamicsAnalysis")


class BevelGearMeshMultibodyDynamicsAnalysis(
    _5388.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
):
    """BevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
            parent: "BevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5388.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5388.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5419.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5445.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(
                _5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5498.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5504.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(
                _5504.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5507.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(
                _5507.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5528.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(_5528.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshMultibodyDynamicsAnalysis.TYPE"
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
    ) -> "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearMeshMultibodyDynamicsAnalysis(self)
