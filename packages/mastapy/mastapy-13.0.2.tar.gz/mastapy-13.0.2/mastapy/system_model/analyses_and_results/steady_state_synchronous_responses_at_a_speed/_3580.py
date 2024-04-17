"""KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3546,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3583,
        _3586,
        _3572,
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed(
    _3546.ConicalGearSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3546.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3546.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3572.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(_3572.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
