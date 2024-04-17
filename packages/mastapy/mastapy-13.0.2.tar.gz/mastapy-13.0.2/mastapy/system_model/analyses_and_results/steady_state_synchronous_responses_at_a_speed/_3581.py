"""KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3578,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.static_loads import _6925
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3544,
        _3570,
        _3577,
        _3547,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3578.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3578.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3578.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3544.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3570.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "_6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed(
            self
        )
