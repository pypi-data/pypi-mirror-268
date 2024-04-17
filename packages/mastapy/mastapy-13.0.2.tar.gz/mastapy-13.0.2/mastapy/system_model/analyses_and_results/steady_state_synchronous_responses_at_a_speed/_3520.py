"""BearingSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3548,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BearingSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.static_loads import _6828
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BearingSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BearingSteadyStateSynchronousResponseAtASpeed")


class BearingSteadyStateSynchronousResponseAtASpeed(
    _3548.ConnectorSteadyStateSynchronousResponseAtASpeed
):
    """BearingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEARING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BearingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BearingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
            parent: "BearingSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3548.ConnectorSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3548.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
        ) -> "BearingSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BearingSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2446.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6828.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[BearingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BearingSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingSteadyStateSynchronousResponseAtASpeed._Cast_BearingSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BearingSteadyStateSynchronousResponseAtASpeed(self)
