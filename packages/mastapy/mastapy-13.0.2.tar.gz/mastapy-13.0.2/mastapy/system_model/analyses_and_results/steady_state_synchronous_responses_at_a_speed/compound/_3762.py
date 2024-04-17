"""TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3681,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3633,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3719,
        _3667,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
)


class TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed(
    _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
):
    """TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _TORQUE_CONVERTER_TURBINE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3681.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "List[_3633.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3633.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
