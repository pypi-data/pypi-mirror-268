"""HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3516,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3544,
        _3570,
        _3577,
        _3547,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="HypoidGearMeshSteadyStateSynchronousResponseAtASpeed")


class HypoidGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3516.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """HypoidGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting HypoidGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3516.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3516.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3544.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3570.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6915.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed(self)
