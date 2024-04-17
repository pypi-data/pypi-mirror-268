"""MassDiscSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3117,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "MassDiscSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6930
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3069,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MassDiscSteadyStateSynchronousResponse")


class MassDiscSteadyStateSynchronousResponse(
    _3117.VirtualComponentSteadyStateSynchronousResponse
):
    """MassDiscSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscSteadyStateSynchronousResponse"
    )

    class _Cast_MassDiscSteadyStateSynchronousResponse:
        """Special nested class for casting MassDiscSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
            parent: "MassDiscSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3117.VirtualComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3117.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "MassDiscSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "MassDiscSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6930.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MassDiscSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse":
        return self._Cast_MassDiscSteadyStateSynchronousResponse(self)
