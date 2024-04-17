"""ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3443,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3286,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3389,
        _3396,
        _3401,
        _3447,
        _3451,
        _3454,
        _3457,
        _3484,
        _3490,
        _3493,
        _3511,
        _3481,
        _3383,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
)


class ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3443.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3443.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3443.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3481.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3389.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3389,
            )

            return self._parent._cast(
                _3389.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3401.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3447.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3451.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3457.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3484.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3490.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3493.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3511.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3511,
            )

            return self._parent._cast(
                _3511.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSetSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSetSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
