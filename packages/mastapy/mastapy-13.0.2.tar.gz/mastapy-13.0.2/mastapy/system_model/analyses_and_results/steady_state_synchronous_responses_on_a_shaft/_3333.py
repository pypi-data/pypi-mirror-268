"""PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3290,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3318,
        _3288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)


class PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3290.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(
        self: Self,
    ) -> "_6938.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

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
    ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
