"""CycloidalDiscSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2993,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CycloidalDiscSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2992,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CycloidalDiscSteadyStateSynchronousResponse")


class CycloidalDiscSteadyStateSynchronousResponse(
    _2993.AbstractShaftSteadyStateSynchronousResponse
):
    """CycloidalDiscSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscSteadyStateSynchronousResponse"
    )

    class _Cast_CycloidalDiscSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
            parent: "CycloidalDiscSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2993.AbstractShaftSteadyStateSynchronousResponse":
            return self._parent._cast(_2993.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2992.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CycloidalDiscSteadyStateSynchronousResponse.TYPE"
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
    def component_load_case(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscSteadyStateSynchronousResponse(self)
