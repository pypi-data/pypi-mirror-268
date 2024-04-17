"""PlanetCarrierCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3201,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PlanetCarrierCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3077,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3149,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundSteadyStateSynchronousResponse")


class PlanetCarrierCompoundSteadyStateSynchronousResponse(
    _3201.MountableComponentCompoundSteadyStateSynchronousResponse
):
    """PlanetCarrierCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetCarrierCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
            parent: "PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.MountableComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3201.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
        ) -> "PlanetCarrierCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetCarrierCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2476.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3077.PlanetCarrierSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetCarrierSteadyStateSynchronousResponse]

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
    ) -> "List[_3077.PlanetCarrierSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetCarrierSteadyStateSynchronousResponse]

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
    ) -> "PlanetCarrierCompoundSteadyStateSynchronousResponse._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse":
        return self._Cast_PlanetCarrierCompoundSteadyStateSynchronousResponse(self)
