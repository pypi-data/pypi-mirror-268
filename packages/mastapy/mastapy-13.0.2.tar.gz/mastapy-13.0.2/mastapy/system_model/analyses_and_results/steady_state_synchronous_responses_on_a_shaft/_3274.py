"""ClutchConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3290,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3318,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ClutchConnectionSteadyStateSynchronousResponseOnAShaft")


class ClutchConnectionSteadyStateSynchronousResponseOnAShaft(
    _3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
):
    """ClutchConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ClutchConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ClutchConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2349.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6841.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

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
    ) -> "ClutchConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ClutchConnectionSteadyStateSynchronousResponseOnAShaft(self)
