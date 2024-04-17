"""ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3702,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3545,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3648,
        _3655,
        _3660,
        _3706,
        _3710,
        _3713,
        _3716,
        _3743,
        _3749,
        _3752,
        _3770,
        _3740,
        _3642,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
)


class ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3648.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3648,
            )

            return self._parent._cast(
                _3648.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3655.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3660.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3706.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3710.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3716.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3743.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3749.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3752.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3770.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3770,
            )

            return self._parent._cast(
                _3770.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
