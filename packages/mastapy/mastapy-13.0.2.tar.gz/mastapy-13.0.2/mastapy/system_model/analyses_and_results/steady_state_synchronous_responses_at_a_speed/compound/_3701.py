"""GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3707,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3570,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3647,
        _3654,
        _3659,
        _3672,
        _3675,
        _3690,
        _3696,
        _3705,
        _3709,
        _3712,
        _3715,
        _3742,
        _3748,
        _3751,
        _3766,
        _3769,
        _3677,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="GearMeshCompoundSteadyStateSynchronousResponseAtASpeed")


class GearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
    _3707.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """GearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting GearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3707.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3707.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3647.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3647,
            )

            return self._parent._cast(
                _3647.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3654.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3654,
            )

            return self._parent._cast(
                _3654.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3659.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3672.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3675.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3675,
            )

            return self._parent._cast(
                _3675.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3696.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3696,
            )

            return self._parent._cast(
                _3696.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3705.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3709.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3712.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3712,
            )

            return self._parent._cast(
                _3712.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3742.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3742,
            )

            return self._parent._cast(
                _3742.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3748.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3751.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3766.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3766,
            )

            return self._parent._cast(
                _3766.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3769.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3769,
            )

            return self._parent._cast(
                _3769.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3570.GearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3570.GearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_GearMeshCompoundSteadyStateSynchronousResponseAtASpeed(self)
