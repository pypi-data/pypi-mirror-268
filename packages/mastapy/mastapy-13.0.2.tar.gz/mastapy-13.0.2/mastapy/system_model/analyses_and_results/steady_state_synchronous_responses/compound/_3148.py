"""CoaxialConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3221,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3015,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3168,
        _3127,
        _3159,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundSteadyStateSynchronousResponse")


class CoaxialConnectionCompoundSteadyStateSynchronousResponse(
    _3221.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """CoaxialConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CoaxialConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
            parent: "CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3221.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3221.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3127.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3127,
            )

            return self._parent._cast(
                _3127.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3168.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CoaxialConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3015.CoaxialConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CoaxialConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3015.CoaxialConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CoaxialConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponse._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponse(self)
