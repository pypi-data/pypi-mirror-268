"""CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3430,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3303,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3441,
        _3460,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = (
        _CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3430.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3303.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3303.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
