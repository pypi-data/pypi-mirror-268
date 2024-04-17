"""ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3441,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3287,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3387,
        _3394,
        _3397,
        _3398,
        _3399,
        _3445,
        _3449,
        _3452,
        _3455,
        _3482,
        _3488,
        _3491,
        _3494,
        _3495,
        _3509,
        _3460,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
)


class ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3394,
            )

            return self._parent._cast(
                _3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3287.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3287.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
