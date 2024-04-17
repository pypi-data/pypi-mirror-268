"""PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3350,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3256,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft"
)


class PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft(
    _3350.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3350.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3350.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3256.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2294.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6941.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
