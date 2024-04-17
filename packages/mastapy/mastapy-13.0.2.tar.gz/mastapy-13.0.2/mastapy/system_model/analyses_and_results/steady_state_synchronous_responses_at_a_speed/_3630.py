"""TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3549,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3577,
        _3547,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"
)


class TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed(
    _3549.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
):
    """TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3549.CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3549.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
