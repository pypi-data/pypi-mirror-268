"""BoltSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3278,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BoltSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="BoltSteadyStateSynchronousResponseOnAShaft")


class BoltSteadyStateSynchronousResponseOnAShaft(
    _3278.ComponentSteadyStateSynchronousResponseOnAShaft
):
    """BoltSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_BoltSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BoltSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
            parent: "BoltSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
        ) -> "BoltSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "BoltSteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2449.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6840.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

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
    ) -> "BoltSteadyStateSynchronousResponseOnAShaft._Cast_BoltSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BoltSteadyStateSynchronousResponseOnAShaft(self)
