"""CVTSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3522,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CVTSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3610,
        _3512,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CVTSteadyStateSynchronousResponseAtASpeed")


class CVTSteadyStateSynchronousResponseAtASpeed(
    _3522.BeltDriveSteadyStateSynchronousResponseAtASpeed
):
    """CVTSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CVTSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
            parent: "CVTSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3522.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3522.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
        ) -> "CVTSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "CVTSteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.CVT":
        """mastapy.system_model.part_model.couplings.CVT

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
    ) -> "CVTSteadyStateSynchronousResponseAtASpeed._Cast_CVTSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CVTSteadyStateSynchronousResponseAtASpeed(self)
