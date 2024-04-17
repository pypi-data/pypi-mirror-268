"""ClutchSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3292,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ClutchSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2585
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3351,
        _3253,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ClutchSteadyStateSynchronousResponseOnAShaft")


class ClutchSteadyStateSynchronousResponseOnAShaft(
    _3292.CouplingSteadyStateSynchronousResponseOnAShaft
):
    """ClutchSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CLUTCH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ClutchSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ClutchSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
            parent: "ClutchSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3292.CouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3292.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
        ) -> "ClutchSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ClutchSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2585.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchSteadyStateSynchronousResponseOnAShaft._Cast_ClutchSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ClutchSteadyStateSynchronousResponseOnAShaft(self)
