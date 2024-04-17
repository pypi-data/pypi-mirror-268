"""ClutchHalfModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ClutchHalfModalAnalysisAtASpeed")


class ClutchHalfModalAnalysisAtASpeed(_5163.CouplingHalfModalAnalysisAtASpeed):
    """ClutchHalfModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfModalAnalysisAtASpeed")

    class _Cast_ClutchHalfModalAnalysisAtASpeed:
        """Special nested class for casting ClutchHalfModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
            parent: "ClutchHalfModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_5163.CouplingHalfModalAnalysisAtASpeed":
            return self._parent._cast(_5163.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
        ) -> "ClutchHalfModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6842.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

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
    ) -> "ClutchHalfModalAnalysisAtASpeed._Cast_ClutchHalfModalAnalysisAtASpeed":
        return self._Cast_ClutchHalfModalAnalysisAtASpeed(self)
