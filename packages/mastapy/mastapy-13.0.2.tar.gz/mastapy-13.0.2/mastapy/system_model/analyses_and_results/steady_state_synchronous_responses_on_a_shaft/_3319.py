"""KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3285,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3322,
        _3325,
        _3311,
        _3318,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)


class KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3285.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3285.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3311.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
            self
        )
