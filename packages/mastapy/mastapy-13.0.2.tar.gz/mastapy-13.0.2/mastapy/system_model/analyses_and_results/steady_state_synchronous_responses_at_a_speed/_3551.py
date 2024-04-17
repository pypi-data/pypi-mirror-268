"""CouplingSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3610,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CouplingSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3535,
        _3540,
        _3594,
        _3616,
        _3632,
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CouplingSteadyStateSynchronousResponseAtASpeed")


class CouplingSteadyStateSynchronousResponseAtASpeed(
    _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
):
    """CouplingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CouplingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3535.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingSteadyStateSynchronousResponseAtASpeed._Cast_CouplingSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CouplingSteadyStateSynchronousResponseAtASpeed(self)
