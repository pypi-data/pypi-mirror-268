"""AGMAGleasonConicalGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3004,
        _3005,
        _3006,
        _3009,
        _3056,
        _3093,
        _3102,
        _3105,
        _3106,
        _3107,
        _3123,
        _3052,
        _3069,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSteadyStateSynchronousResponse")


class AGMAGleasonConicalGearSteadyStateSynchronousResponse(
    _3025.ConicalGearSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse"
    )

    class _Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3025.ConicalGearSteadyStateSynchronousResponse":
            return self._parent._cast(_3025.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3052.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(_3052.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3004.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3006.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3009.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(_3009.BevelGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3056.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(_3056.HypoidGearSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3093.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3102.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3105.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3106.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3107.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3123.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse(self)
