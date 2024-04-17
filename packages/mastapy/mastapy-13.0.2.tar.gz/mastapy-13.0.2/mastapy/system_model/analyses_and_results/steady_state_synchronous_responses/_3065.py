"""KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3059,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3066,
        _3064,
        _3024,
        _3051,
        _3090,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse(
    _3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> (
            "_3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            return self._parent._cast(
                _3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3024.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3051.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(_3051.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3066.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse(
            self
        )
