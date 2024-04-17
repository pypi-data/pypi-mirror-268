"""SynchroniserSleeveSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3109,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SynchroniserSleeveSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.static_loads import _6979
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3029,
        _3069,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserSleeveSteadyStateSynchronousResponse")


class SynchroniserSleeveSteadyStateSynchronousResponse(
    _3109.SynchroniserPartSteadyStateSynchronousResponse
):
    """SynchroniserSleeveSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveSteadyStateSynchronousResponse"
    )

    class _Cast_SynchroniserSleeveSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserSleeveSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
            parent: "SynchroniserSleeveSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3109.SynchroniserPartSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3109.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3029.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "SynchroniserSleeveSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserSleeveSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6979.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserSleeveSteadyStateSynchronousResponse(self)
