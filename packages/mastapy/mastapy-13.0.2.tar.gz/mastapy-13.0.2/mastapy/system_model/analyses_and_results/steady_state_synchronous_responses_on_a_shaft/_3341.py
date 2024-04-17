"""PulleySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3291,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PulleySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3294,
        _3330,
        _3278,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PulleySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PulleySteadyStateSynchronousResponseOnAShaft")


class PulleySteadyStateSynchronousResponseOnAShaft(
    _3291.CouplingHalfSteadyStateSynchronousResponseOnAShaft
):
    """PulleySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PulleySteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_PulleySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PulleySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
            parent: "PulleySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3291.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3294.CVTPulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3294,
            )

            return self._parent._cast(
                _3294.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "PulleySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PulleySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

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
    ) -> "PulleySteadyStateSynchronousResponseOnAShaft._Cast_PulleySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PulleySteadyStateSynchronousResponseOnAShaft(self)
