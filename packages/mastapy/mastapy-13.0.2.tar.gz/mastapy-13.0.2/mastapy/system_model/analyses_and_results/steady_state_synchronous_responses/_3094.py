"""SpringDamperConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3028,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpringDamperConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2357
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpringDamperConnectionSteadyStateSynchronousResponse")


class SpringDamperConnectionSteadyStateSynchronousResponse(
    _3028.CouplingConnectionSteadyStateSynchronousResponse
):
    """SpringDamperConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_SpringDamperConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting SpringDamperConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
            parent: "SpringDamperConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_3028.CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3028.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
        ) -> "SpringDamperConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpringDamperConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6965.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse":
        return self._Cast_SpringDamperConnectionSteadyStateSynchronousResponse(self)
