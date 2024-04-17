"""CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3730,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3553,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3681,
        _3719,
        _3667,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed")


class CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed(
    _3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3681,
            )

            return self._parent._cast(
                _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3553.CVTPulleySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CVTPulleySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3553.CVTPulleySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CVTPulleySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed(self)
