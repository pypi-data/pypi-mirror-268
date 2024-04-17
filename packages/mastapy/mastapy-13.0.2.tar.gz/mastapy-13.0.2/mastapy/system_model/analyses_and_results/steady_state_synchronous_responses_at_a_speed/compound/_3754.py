"""StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3747,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3625,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3658,
        _3646,
        _3674,
        _3700,
        _3719,
        _3667,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3747.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3747.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent._cast(
                _3747.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3658.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3658,
            )

            return self._parent._cast(
                _3658.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3646.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3674.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3700.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
