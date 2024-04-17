"""ClutchConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3028,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ClutchConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ClutchConnectionSteadyStateSynchronousResponse")


class ClutchConnectionSteadyStateSynchronousResponse(
    _3028.CouplingConnectionSteadyStateSynchronousResponse
):
    """ClutchConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_ClutchConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ClutchConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
            parent: "ClutchConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_3028.CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3028.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "ClutchConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ClutchConnectionSteadyStateSynchronousResponse.TYPE",
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
    ) -> "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse":
        return self._Cast_ClutchConnectionSteadyStateSynchronousResponse(self)
