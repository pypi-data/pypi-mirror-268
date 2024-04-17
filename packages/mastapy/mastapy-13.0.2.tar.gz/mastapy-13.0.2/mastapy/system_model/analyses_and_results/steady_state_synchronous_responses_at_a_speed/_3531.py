"""BoltedJointSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3610,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BoltedJointSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BoltedJointSteadyStateSynchronousResponseAtASpeed")


class BoltedJointSteadyStateSynchronousResponseAtASpeed(
    _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
):
    """BoltedJointSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BoltedJointSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
            parent: "BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
        ) -> "BoltedJointSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BoltedJointSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2450.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6839.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointSteadyStateSynchronousResponseAtASpeed._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BoltedJointSteadyStateSynchronousResponseAtASpeed(self)
