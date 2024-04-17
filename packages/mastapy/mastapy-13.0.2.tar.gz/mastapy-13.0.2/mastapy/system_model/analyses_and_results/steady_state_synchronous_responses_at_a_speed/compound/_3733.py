"""RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3740,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3603,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3642,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"
)


class RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(
    _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
):
    """RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
