"""CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3460,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3291,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3406,
        _3411,
        _3425,
        _3465,
        _3471,
        _3475,
        _3487,
        _3497,
        _3498,
        _3499,
        _3502,
        _3503,
        _3408,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(
    _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3460.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3291.CouplingHalfSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3291.CouplingHalfSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
