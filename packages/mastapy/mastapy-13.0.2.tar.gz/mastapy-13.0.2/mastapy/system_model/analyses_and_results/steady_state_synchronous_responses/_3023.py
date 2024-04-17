"""ConicalGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3050,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConicalGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2314
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2995,
        _3002,
        _3007,
        _3054,
        _3058,
        _3061,
        _3064,
        _3091,
        _3100,
        _3103,
        _3121,
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearMeshSteadyStateSynchronousResponse")


class ConicalGearMeshSteadyStateSynchronousResponse(
    _3050.GearMeshSteadyStateSynchronousResponse
):
    """ConicalGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
            parent: "ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3050.GearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(_3050.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3007.BevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(_3007.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3054.HypoidGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
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
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3091.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3103.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3121.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "ConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
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
        self: Self,
        instance_to_wrap: "ConicalGearMeshSteadyStateSynchronousResponse.TYPE",
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
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearMeshSteadyStateSynchronousResponse(self)
