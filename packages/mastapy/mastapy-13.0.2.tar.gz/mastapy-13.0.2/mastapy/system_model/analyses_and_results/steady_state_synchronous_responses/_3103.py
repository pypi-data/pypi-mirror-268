"""StraightBevelGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2334
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2995,
        _3023,
        _3050,
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelGearMeshSteadyStateSynchronousResponse")


class StraightBevelGearMeshSteadyStateSynchronousResponse(
    _3007.BevelGearMeshSteadyStateSynchronousResponse
):
    """StraightBevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
            parent: "StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3007.BevelGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(_3007.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3023.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3050.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(_3050.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6972.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

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
    ) -> "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse(self)
