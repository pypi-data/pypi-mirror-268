"""GearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "GearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2997,
        _3004,
        _3005,
        _3006,
        _3009,
        _3022,
        _3025,
        _3040,
        _3041,
        _3047,
        _3056,
        _3060,
        _3063,
        _3066,
        _3093,
        _3102,
        _3105,
        _3106,
        _3107,
        _3120,
        _3123,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GearSteadyStateSynchronousResponse")


class GearSteadyStateSynchronousResponse(
    _3069.MountableComponentSteadyStateSynchronousResponse
):
    """GearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSteadyStateSynchronousResponse")

    class _Cast_GearSteadyStateSynchronousResponse:
        """Special nested class for casting GearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
            parent: "GearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(
                _2997.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3004.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3006.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3009.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(_3009.BevelGearSteadyStateSynchronousResponse)

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3022.ConceptGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3025.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.ConicalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3040.CylindricalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(
                _3040.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3041.CylindricalPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(
                _3041.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def face_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3047.FaceGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(_3047.FaceGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3056.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(_3056.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3060.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(
                _3060.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3063.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3066.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3093.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3102.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3105.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3106.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3107.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3120.WormGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3120,
            )

            return self._parent._cast(_3120.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "_3123.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def gear_steady_state_synchronous_response(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
        ) -> "GearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "GearSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.Gear":
        """mastapy.system_model.part_model.gears.Gear

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
    ) -> "GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse":
        return self._Cast_GearSteadyStateSynchronousResponse(self)
