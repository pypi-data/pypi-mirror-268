"""HypoidGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3257,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3285,
        _3311,
        _3318,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="HypoidGearMeshSteadyStateSynchronousResponseOnAShaft")


class HypoidGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3257.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """HypoidGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting HypoidGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3257.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3311.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "HypoidGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_HypoidGearMeshSteadyStateSynchronousResponseOnAShaft(self)
