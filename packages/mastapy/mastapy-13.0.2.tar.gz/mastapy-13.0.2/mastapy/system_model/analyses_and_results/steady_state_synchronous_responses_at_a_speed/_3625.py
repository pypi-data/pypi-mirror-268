"""StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3620,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3530,
        _3518,
        _3546,
        _3572,
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed(
    _3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3530.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3546.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3572.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(_3572.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
