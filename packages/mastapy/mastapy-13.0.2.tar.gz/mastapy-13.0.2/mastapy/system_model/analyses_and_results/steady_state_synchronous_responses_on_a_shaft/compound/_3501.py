"""TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3421,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3371,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3448,
        _3418,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


class TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3421.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3421.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3421.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3448.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3371.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3371.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
