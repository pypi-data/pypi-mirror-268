"""VirtualComponentSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3589,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3587,
        _3588,
        _3598,
        _3599,
        _3634,
        _3537,
        _3591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentSteadyStateSynchronousResponseAtASpeed")


class VirtualComponentSteadyStateSynchronousResponseAtASpeed(
    _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
):
    """VirtualComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting VirtualComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3589.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3588.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3598.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3634.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3634,
            )

            return self._parent._cast(
                _3634.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "VirtualComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed(self)
