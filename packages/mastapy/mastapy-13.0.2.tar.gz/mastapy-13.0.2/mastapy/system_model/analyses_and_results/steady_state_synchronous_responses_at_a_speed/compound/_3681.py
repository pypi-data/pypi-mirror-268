"""CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3719,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3550,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3665,
        _3670,
        _3684,
        _3724,
        _3730,
        _3734,
        _3746,
        _3756,
        _3757,
        _3758,
        _3761,
        _3762,
        _3667,
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
    _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3719.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3665.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3670.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3684.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3724.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3746.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3756.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3757.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3757,
            )

            return self._parent._cast(
                _3757.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3758.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3761.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3762.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3762,
            )

            return self._parent._cast(
                _3762.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3550.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
