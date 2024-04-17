"""PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3162,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3072,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3189,
        _3159,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
)


class PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse(
    _3162.CouplingConnectionCompoundSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3162.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "List[_3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse]

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
    ) -> "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
