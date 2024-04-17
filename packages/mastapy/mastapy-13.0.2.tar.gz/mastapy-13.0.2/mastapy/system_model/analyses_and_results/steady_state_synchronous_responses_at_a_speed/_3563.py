"""DatumSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3537,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "DatumSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6878
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("DatumSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="DatumSteadyStateSynchronousResponseAtASpeed")


class DatumSteadyStateSynchronousResponseAtASpeed(
    _3537.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """DatumSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _DATUM_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DatumSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_DatumSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting DatumSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
            parent: "DatumSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
        ) -> "DatumSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "DatumSteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6878.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DatumSteadyStateSynchronousResponseAtASpeed._Cast_DatumSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_DatumSteadyStateSynchronousResponseAtASpeed(self)
