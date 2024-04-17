"""StraightBevelSunGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3229,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3107,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3140,
        _3128,
        _3156,
        _3182,
        _3201,
        _3149,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearCompoundSteadyStateSynchronousResponse"
)


class StraightBevelSunGearCompoundSteadyStateSynchronousResponse(
    _3229.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
):
    """StraightBevelSunGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelSunGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3229.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3229.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3128.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3182.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(_3182.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3107.StraightBevelSunGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelSunGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3107.StraightBevelSunGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelSunGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse(
            self
        )
