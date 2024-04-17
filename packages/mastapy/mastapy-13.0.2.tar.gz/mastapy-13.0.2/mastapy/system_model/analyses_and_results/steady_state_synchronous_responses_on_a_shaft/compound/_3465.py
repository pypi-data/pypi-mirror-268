"""PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3422,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3334,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3460,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(
    _3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3422.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
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
        "List[_3334.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
        "List[_3334.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
