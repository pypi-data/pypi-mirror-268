"""CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3666,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3556,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3739,
        _3645,
        _3677,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)


class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3666.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3666.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3666.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3739.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3739,
            )

            return self._parent._cast(
                _3739.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3645.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3645,
            )

            return self._parent._cast(
                _3645.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3556.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3556.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
