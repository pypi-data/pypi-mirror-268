"""AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3278,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3255,
        _3299,
        _3309,
        _3349,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft"
)


class AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft(
    _3278.ComponentSteadyStateSynchronousResponseOnAShaft
):
    """AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3255.AbstractShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.CycloidalDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3309.FEPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.ShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(_3349.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2443.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft(
            self
        )
