"""BeltConnectionSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3577,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.static_loads import _6829
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3552,
        _3547,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BeltConnectionSteadyStateSynchronousResponseAtASpeed")


class BeltConnectionSteadyStateSynchronousResponseAtASpeed(
    _3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """BeltConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BeltConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "BeltConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BeltConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6829.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

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
    ) -> "BeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BeltConnectionSteadyStateSynchronousResponseAtASpeed(self)
