"""StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3529,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3623,
        _3621,
        _3517,
        _3545,
        _3571,
        _3610,
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed(
    _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6973.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3623.StraightBevelGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3621.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed(
            self
        )
