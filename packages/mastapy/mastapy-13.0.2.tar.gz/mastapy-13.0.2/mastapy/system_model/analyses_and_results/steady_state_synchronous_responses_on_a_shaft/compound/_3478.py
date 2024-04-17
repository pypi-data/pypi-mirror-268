"""ShaftCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3384,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3349,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3385,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ShaftCompoundSteadyStateSynchronousResponseOnAShaft")


class ShaftCompoundSteadyStateSynchronousResponseOnAShaft(
    _3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ShaftCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ShaftCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3384.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3385.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ShaftCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

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
    ) -> "List[_3349.ShaftSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ShaftSteadyStateSynchronousResponseOnAShaft]

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
    def planetaries(
        self: Self,
    ) -> "List[ShaftCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ShaftCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3349.ShaftSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ShaftSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ShaftCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ShaftCompoundSteadyStateSynchronousResponseOnAShaft(self)
