"""TorqueConverterTurbineCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3163,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3115,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3201,
        _3149,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="TorqueConverterTurbineCompoundSteadyStateSynchronousResponse"
)


class TorqueConverterTurbineCompoundSteadyStateSynchronousResponse(
    _3163.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """TorqueConverterTurbineCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterTurbineCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
            parent: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.CouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3163.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
        ) -> "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_3115.TorqueConverterTurbineSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterTurbineSteadyStateSynchronousResponse]

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
    ) -> "List[_3115.TorqueConverterTurbineSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterTurbineSteadyStateSynchronousResponse]

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
    ) -> "TorqueConverterTurbineCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponse(
            self
        )
