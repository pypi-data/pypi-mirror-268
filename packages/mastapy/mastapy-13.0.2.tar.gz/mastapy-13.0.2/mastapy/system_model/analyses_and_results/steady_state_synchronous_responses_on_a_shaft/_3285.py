"""ConicalGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3311,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2314
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3257,
        _3264,
        _3269,
        _3315,
        _3319,
        _3322,
        _3325,
        _3352,
        _3359,
        _3362,
        _3380,
        _3318,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConicalGearMeshSteadyStateSynchronousResponseOnAShaft")


class ConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3311.GearMeshSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3311.GearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3311.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3264.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3269.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3315.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3319.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3359.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3380.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3380,
            )

            return self._parent._cast(
                _3380.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "List[ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearMeshSteadyStateSynchronousResponseOnAShaft(self)
