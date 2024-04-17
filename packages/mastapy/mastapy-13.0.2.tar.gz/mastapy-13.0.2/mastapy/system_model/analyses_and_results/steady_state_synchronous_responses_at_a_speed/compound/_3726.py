"""PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3691,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3596,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3702,
        _3740,
        _3642,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
)


class PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3691.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3691.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
