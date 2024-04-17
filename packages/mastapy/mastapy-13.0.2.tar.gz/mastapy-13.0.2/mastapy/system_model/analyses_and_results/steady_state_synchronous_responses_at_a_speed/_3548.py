"""ConnectorSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3589,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConnectorSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3520,
        _3590,
        _3607,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConnectorSteadyStateSynchronousResponseAtASpeed")


class ConnectorSteadyStateSynchronousResponseAtASpeed(
    _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
):
    """ConnectorSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConnectorSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConnectorSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
            parent: "ConnectorSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3520.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3590.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConnectorSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConnectorSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConnectorSteadyStateSynchronousResponseAtASpeed(self)
