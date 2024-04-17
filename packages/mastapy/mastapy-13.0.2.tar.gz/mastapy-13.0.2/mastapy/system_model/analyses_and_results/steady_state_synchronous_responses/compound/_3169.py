"""CycloidalDiscCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3125,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CycloidalDiscCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3037,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3126,
        _3149,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundSteadyStateSynchronousResponse")


class CycloidalDiscCompoundSteadyStateSynchronousResponse(
    _3125.AbstractShaftCompoundSteadyStateSynchronousResponse
):
    """CycloidalDiscCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
            parent: "CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3125.AbstractShaftCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3125.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3126.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CycloidalDiscCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_3037.CycloidalDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscSteadyStateSynchronousResponse]

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
    ) -> "List[_3037.CycloidalDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscSteadyStateSynchronousResponse]

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
    ) -> "CycloidalDiscCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponse(self)
