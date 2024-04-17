"""PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3480,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3336,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3386,
        _3418,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
)


class PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3480.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3480.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3480.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3386.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3386,
            )

            return self._parent._cast(
                _3386.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2294.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3336.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3336.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
