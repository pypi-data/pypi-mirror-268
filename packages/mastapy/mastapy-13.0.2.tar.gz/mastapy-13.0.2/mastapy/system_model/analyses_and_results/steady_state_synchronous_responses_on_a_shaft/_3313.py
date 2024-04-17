"""GearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3330,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "GearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3259,
        _3266,
        _3267,
        _3268,
        _3271,
        _3284,
        _3287,
        _3302,
        _3303,
        _3308,
        _3317,
        _3321,
        _3324,
        _3327,
        _3354,
        _3361,
        _3364,
        _3365,
        _3366,
        _3379,
        _3382,
        _3278,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="GearSteadyStateSynchronousResponseOnAShaft")


class GearSteadyStateSynchronousResponseOnAShaft(
    _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """GearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_GearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting GearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
            parent: "GearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3259.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3267.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3271.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3284.ConceptGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.CylindricalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3303.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.FaceGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3317.HypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3321.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3354.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3361.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3364.StraightBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3365.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3379.WormGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3379,
            )

            return self._parent._cast(
                _3379.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3382.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3382,
            )

            return self._parent._cast(
                _3382.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
        ) -> "GearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "GearSteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.Gear":
        """mastapy.system_model.part_model.gears.Gear

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
    ) -> "GearSteadyStateSynchronousResponseOnAShaft._Cast_GearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_GearSteadyStateSynchronousResponseOnAShaft(self)
