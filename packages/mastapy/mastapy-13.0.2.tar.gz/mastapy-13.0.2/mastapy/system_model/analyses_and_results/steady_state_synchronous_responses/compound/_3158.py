"""ConicalGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3184,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConicalGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3024,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3130,
        _3137,
        _3142,
        _3188,
        _3192,
        _3195,
        _3198,
        _3225,
        _3231,
        _3234,
        _3252,
        _3222,
        _3124,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundSteadyStateSynchronousResponse")


class ConicalGearSetCompoundSteadyStateSynchronousResponse(
    _3184.GearSetCompoundSteadyStateSynchronousResponse
):
    """ConicalGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
            parent: "ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.GearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3184.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3142.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3188.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3192.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3252,
            )

            return self._parent._cast(
                _3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConicalGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3024.ConicalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3024.ConicalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponse(self)
