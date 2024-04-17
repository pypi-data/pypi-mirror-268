"""KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3286,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3323,
        _3326,
        _3312,
        _3351,
        _3253,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)


class KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3286.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3323.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft(
            self
        )
