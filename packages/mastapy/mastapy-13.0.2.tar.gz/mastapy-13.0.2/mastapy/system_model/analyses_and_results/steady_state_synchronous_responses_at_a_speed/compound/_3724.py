"""PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3681,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3593,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3719,
        _3667,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
    _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> (
        "List[_3593.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
        "List[_3593.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
