"""ConicalGearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3571,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3517,
        _3524,
        _3529,
        _3575,
        _3579,
        _3582,
        _3585,
        _3612,
        _3619,
        _3622,
        _3640,
        _3610,
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearSetSteadyStateSynchronousResponseAtASpeed")


class ConicalGearSetSteadyStateSynchronousResponseAtASpeed(
    _3571.GearSetSteadyStateSynchronousResponseAtASpeed
):
    """ConicalGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.GearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3571.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2531.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed(self)
