"""SpiralBevelGearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3271,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3259,
        _3287,
        _3313,
        _3330,
        _3278,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SpiralBevelGearSteadyStateSynchronousResponseOnAShaft")


class SpiralBevelGearSteadyStateSynchronousResponseOnAShaft(
    _3271.BevelGearSteadyStateSynchronousResponseOnAShaft
):
    """SpiralBevelGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpiralBevelGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
            parent: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3271.BevelGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3271.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3259.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3313.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(_3313.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6962.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft(self)
