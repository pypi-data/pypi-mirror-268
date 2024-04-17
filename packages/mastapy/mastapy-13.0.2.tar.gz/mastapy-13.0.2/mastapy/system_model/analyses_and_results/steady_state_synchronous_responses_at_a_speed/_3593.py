"""PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3550,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"
)


class PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed(
    _3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
            parent: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed(
            self
        )
