"""ConicalGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3572,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConicalGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3518,
        _3525,
        _3526,
        _3527,
        _3530,
        _3576,
        _3580,
        _3583,
        _3586,
        _3613,
        _3620,
        _3623,
        _3624,
        _3625,
        _3641,
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearSteadyStateSynchronousResponseAtASpeed")


class ConicalGearSteadyStateSynchronousResponseAtASpeed(
    _3572.GearSteadyStateSynchronousResponseAtASpeed
):
    """ConicalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
            parent: "ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3572.GearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3572.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3526.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3527.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3530.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3576.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3613.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3624.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3641.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConicalGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConicalGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed(self)
