"""PlanetCarrierSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3330,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3278,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PlanetCarrierSteadyStateSynchronousResponseOnAShaft")


class PlanetCarrierSteadyStateSynchronousResponseOnAShaft(
    _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """PlanetCarrierSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetCarrierSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
            parent: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3330.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3330.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
        ) -> "PlanetCarrierSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PlanetCarrierSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    def component_load_case(self: Self) -> "_6944.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft(self)
