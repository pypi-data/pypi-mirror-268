"""CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3256,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6869
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)


class CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3256.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3256.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3256.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6869.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
