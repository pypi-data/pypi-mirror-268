"""ConnectorSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConnectorSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2999,
        _3070,
        _3087,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConnectorSteadyStateSynchronousResponse")


class ConnectorSteadyStateSynchronousResponse(
    _3069.MountableComponentSteadyStateSynchronousResponse
):
    """ConnectorSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorSteadyStateSynchronousResponse"
    )

    class _Cast_ConnectorSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectorSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
            parent: "ConnectorSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2999.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BearingSteadyStateSynchronousResponse)

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3070.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.OilSealSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3087.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(
                _3087.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def connector_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "ConnectorSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConnectorSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse":
        return self._Cast_ConnectorSteadyStateSynchronousResponse(self)
