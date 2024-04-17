"""AbstractShaftSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3254,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractShaftSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3299,
        _3349,
        _3278,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="AbstractShaftSteadyStateSynchronousResponseOnAShaft")


class AbstractShaftSteadyStateSynchronousResponseOnAShaft(
    _3254.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
):
    """AbstractShaftSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractShaftSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3254.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3254.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.CycloidalDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.ShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(_3349.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractShaftSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractShaftSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractShaftSteadyStateSynchronousResponseOnAShaft(self)
