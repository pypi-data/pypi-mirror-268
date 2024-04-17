"""ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2994,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2302
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3015,
        _3035,
        _3075,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"
)


class ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
    _2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3015.CoaxialConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(
                _3015.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> (
            "_3035.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(
                _3035.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3075.PlanetaryConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2302.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
            self
        )
