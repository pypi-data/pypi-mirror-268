"""BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3394,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3267,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3399,
        _3387,
        _3415,
        _3441,
        _3460,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)


class BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent._cast(
                _3394.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> (
        "List[_3267.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3267.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
