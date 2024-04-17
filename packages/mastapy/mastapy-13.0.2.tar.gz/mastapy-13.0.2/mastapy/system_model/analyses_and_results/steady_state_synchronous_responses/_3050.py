"""GearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "GearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2995,
        _3002,
        _3007,
        _3020,
        _3023,
        _3038,
        _3045,
        _3054,
        _3058,
        _3061,
        _3064,
        _3091,
        _3100,
        _3103,
        _3118,
        _3121,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GearMeshSteadyStateSynchronousResponse")


class GearMeshSteadyStateSynchronousResponse(
    _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """GearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_GearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting GearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
            parent: "GearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3007.BevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(_3007.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3020.ConceptGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(
                _3020.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3023.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3038.CylindricalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(
                _3038.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3045.FaceGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3054.HypoidGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> (
            "_3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(
                _3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3091.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3103.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3118.WormGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3118,
            )

            return self._parent._cast(_3118.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "_3121.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "GearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "GearMeshSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2320.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse":
        return self._Cast_GearMeshSteadyStateSynchronousResponse(self)
