"""CylindricalGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3572,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3562,
        _3589,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearSteadyStateSynchronousResponseAtASpeed")


class CylindricalGearSteadyStateSynchronousResponseAtASpeed(
    _3572.GearSteadyStateSynchronousResponseAtASpeed
):
    """CylindricalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
            parent: "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3572.GearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3572.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CylindricalGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6870.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

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
    ) -> "List[CylindricalGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CylindricalGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed(self)
