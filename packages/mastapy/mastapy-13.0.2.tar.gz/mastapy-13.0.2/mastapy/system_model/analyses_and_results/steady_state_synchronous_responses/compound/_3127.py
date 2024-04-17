"""AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3159,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2994,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3148,
        _3168,
        _3170,
        _3207,
        _3221,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3159.ConnectionCompoundSteadyStateSynchronousResponse
):
    """AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3148.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3168.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3170.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3207.PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3221.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
