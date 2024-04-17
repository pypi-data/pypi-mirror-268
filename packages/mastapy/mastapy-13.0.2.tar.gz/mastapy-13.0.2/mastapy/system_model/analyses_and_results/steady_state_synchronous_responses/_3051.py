"""GearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3090,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "GearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2996,
        _3003,
        _3008,
        _3021,
        _3024,
        _3039,
        _3046,
        _3055,
        _3059,
        _3062,
        _3065,
        _3076,
        _3092,
        _3101,
        _3104,
        _3119,
        _3122,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GearSetSteadyStateSynchronousResponse")


class GearSetSteadyStateSynchronousResponse(
    _3090.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """GearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetSteadyStateSynchronousResponse"
    )

    class _Cast_GearSetSteadyStateSynchronousResponse:
        """Special nested class for casting GearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
            parent: "GearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_2996.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(
                _2996.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3003.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(
                _3003.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3008.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(_3008.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3021.ConceptGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3024.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3039.CylindricalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3046.FaceGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3055.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(_3055.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> (
            "_3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> (
            "_3062.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3065.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3076.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3092.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3101.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(
                _3101.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3104.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3119.WormGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3119,
            )

            return self._parent._cast(_3119.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "_3122.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3122,
            )

            return self._parent._cast(
                _3122.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
        ) -> "GearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "GearSetSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse":
        return self._Cast_GearSetSteadyStateSynchronousResponse(self)
