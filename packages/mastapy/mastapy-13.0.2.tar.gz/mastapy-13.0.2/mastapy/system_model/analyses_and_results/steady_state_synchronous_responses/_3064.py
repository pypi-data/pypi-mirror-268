"""KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3058,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3023,
        _3050,
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse(
    _3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3023.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3050.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(_3050.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> (
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse(
            self
        )
