"""ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3679,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3540,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3740,
        _3642,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
)


class ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed(
    _3679.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3679.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3679.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

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
    ) -> "List[_3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConceptCouplingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConceptCouplingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
