"""ClutchHalfModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4903,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ClutchHalfModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4944,
        _4890,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ClutchHalfModalAnalysisAtAStiffness")


class ClutchHalfModalAnalysisAtAStiffness(_4903.CouplingHalfModalAnalysisAtAStiffness):
    """ClutchHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfModalAnalysisAtAStiffness")

    class _Cast_ClutchHalfModalAnalysisAtAStiffness:
        """Special nested class for casting ClutchHalfModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
            parent: "ClutchHalfModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_4903.CouplingHalfModalAnalysisAtAStiffness":
            return self._parent._cast(_4903.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_4944.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
        ) -> "ClutchHalfModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ClutchHalfModalAnalysisAtAStiffness.TYPE"
    ):
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
    ) -> (
        "ClutchHalfModalAnalysisAtAStiffness._Cast_ClutchHalfModalAnalysisAtAStiffness"
    ):
        return self._Cast_ClutchHalfModalAnalysisAtAStiffness(self)
