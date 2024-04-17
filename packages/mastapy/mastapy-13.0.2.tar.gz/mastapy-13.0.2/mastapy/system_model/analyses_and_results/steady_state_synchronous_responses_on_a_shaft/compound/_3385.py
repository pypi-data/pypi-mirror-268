"""AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3408,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3254,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3384,
        _3428,
        _3439,
        _3478,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
)


class AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft(
    _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = (
        _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3384,
            )

            return self._parent._cast(
                _3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3428.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3439.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3478.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3254.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3254.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
