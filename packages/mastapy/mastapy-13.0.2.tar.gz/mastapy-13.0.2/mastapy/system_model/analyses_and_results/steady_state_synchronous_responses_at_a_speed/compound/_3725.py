"""PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3739,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3595,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3645,
        _3677,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
)


class PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3739.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3739.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3739.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3645.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3645,
            )

            return self._parent._cast(
                _3645.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "List[_3595.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3595.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
