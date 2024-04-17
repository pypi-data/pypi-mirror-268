"""CouplingConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3012,
        _3017,
        _3072,
        _3094,
        _3112,
        _3026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponse")


class CouplingConnectionSteadyStateSynchronousResponse(
    _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """CouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
            parent: "CouplingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3026.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3012.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3017.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3094.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3112.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2353.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponse(self)
