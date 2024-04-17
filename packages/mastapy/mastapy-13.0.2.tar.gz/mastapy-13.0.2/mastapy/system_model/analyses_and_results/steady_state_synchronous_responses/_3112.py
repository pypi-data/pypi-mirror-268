"""TorqueConverterConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3028,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "TorqueConverterConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3057,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="TorqueConverterConnectionSteadyStateSynchronousResponse")


class TorqueConverterConnectionSteadyStateSynchronousResponse(
    _3028.CouplingConnectionSteadyStateSynchronousResponse
):
    """TorqueConverterConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_TorqueConverterConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
            parent: "TorqueConverterConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_3028.CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3028.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
        ) -> "TorqueConverterConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterConnectionSteadyStateSynchronousResponse(self)
