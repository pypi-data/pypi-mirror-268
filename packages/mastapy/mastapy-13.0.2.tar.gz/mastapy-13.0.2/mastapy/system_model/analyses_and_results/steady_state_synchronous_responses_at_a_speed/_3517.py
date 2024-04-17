"""AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3545,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3524,
        _3529,
        _3575,
        _3612,
        _3619,
        _3622,
        _3640,
        _3571,
        _3610,
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"
)


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed(
    _3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2521.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
