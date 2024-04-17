"""AbstractShaftOrHousingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3016,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractShaftOrHousingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2993,
        _3037,
        _3048,
        _3088,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingSteadyStateSynchronousResponse")


class AbstractShaftOrHousingSteadyStateSynchronousResponse(
    _3016.ComponentSteadyStateSynchronousResponse
):
    """AbstractShaftOrHousingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse"
    )

    class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
            parent: "AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_2993.AbstractShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(_2993.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_3037.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_3048.FEPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(_3048.FEPartSteadyStateSynchronousResponse)

        @property
        def shaft_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "_3088.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(_3088.ShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
        ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftOrHousingSteadyStateSynchronousResponse.TYPE",
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
    ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse(self)
