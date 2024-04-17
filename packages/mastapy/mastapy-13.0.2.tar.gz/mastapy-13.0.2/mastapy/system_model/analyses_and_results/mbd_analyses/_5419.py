"""ConicalGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5445
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2314
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5388,
        _5397,
        _5402,
        _5450,
        _5458,
        _5461,
        _5464,
        _5498,
        _5504,
        _5507,
        _5528,
        _5457,
        _5422,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshMultibodyDynamicsAnalysis")


class ConicalGearMeshMultibodyDynamicsAnalysis(_5445.GearMeshMultibodyDynamicsAnalysis):
    """ConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_ConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5445.GearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5445.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5388.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(
                _5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5402.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(_5402.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5450.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(_5450.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5458.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(
                _5458.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5461.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(
                _5461.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> (
            "_5464.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(
                _5464.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5498.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5504.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(
                _5504.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5507.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(
                _5507.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5528.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(_5528.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "ConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshMultibodyDynamicsAnalysis.TYPE"
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
    def planetaries(self: Self) -> "List[ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearMeshMultibodyDynamicsAnalysis(self)
