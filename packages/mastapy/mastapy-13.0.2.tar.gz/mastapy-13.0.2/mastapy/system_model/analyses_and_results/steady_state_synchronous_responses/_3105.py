"""StraightBevelGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3009,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2997,
        _3025,
        _3052,
        _3069,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelGearSteadyStateSynchronousResponse")


class StraightBevelGearSteadyStateSynchronousResponse(
    _3009.BevelGearSteadyStateSynchronousResponse
):
    """StraightBevelGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelGearSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
            parent: "StraightBevelGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3009.BevelGearSteadyStateSynchronousResponse":
            return self._parent._cast(_3009.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(
                _2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3025.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3052.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(_3052.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

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
    ) -> "StraightBevelGearSteadyStateSynchronousResponse._Cast_StraightBevelGearSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearSteadyStateSynchronousResponse(self)
