"""BevelGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3130,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3008,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3137,
        _3225,
        _3231,
        _3234,
        _3252,
        _3158,
        _3184,
        _3222,
        _3124,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearSetCompoundSteadyStateSynchronousResponse")


class BevelGearSetCompoundSteadyStateSynchronousResponse(
    _3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
):
    """BevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3130.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3252,
            )

            return self._parent._cast(
                _3252.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3008.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

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
    ) -> "List[_3008.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

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
    ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse(self)
