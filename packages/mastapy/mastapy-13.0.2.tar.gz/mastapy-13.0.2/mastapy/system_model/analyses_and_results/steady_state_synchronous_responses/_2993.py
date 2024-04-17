"""AbstractShaftSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2992,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractShaftSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3037,
        _3088,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractShaftSteadyStateSynchronousResponse")


class AbstractShaftSteadyStateSynchronousResponse(
    _2992.AbstractShaftOrHousingSteadyStateSynchronousResponse
):
    """AbstractShaftSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftSteadyStateSynchronousResponse"
    )

    class _Cast_AbstractShaftSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
            parent: "AbstractShaftSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2992.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            return self._parent._cast(
                _2992.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3037.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def shaft_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3088.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(_3088.ShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "AbstractShaftSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "AbstractShaftSteadyStateSynchronousResponse.TYPE"
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
    ) -> "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftSteadyStateSynchronousResponse(self)
