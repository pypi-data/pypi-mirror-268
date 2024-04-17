"""UnbalancedMassModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4989,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "UnbalancedMassModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4944,
        _4890,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="UnbalancedMassModalAnalysisAtAStiffness")


class UnbalancedMassModalAnalysisAtAStiffness(
    _4989.VirtualComponentModalAnalysisAtAStiffness
):
    """UnbalancedMassModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassModalAnalysisAtAStiffness"
    )

    class _Cast_UnbalancedMassModalAnalysisAtAStiffness:
        """Special nested class for casting UnbalancedMassModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
            parent: "UnbalancedMassModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_4989.VirtualComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4989.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_4944.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
        ) -> "UnbalancedMassModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "UnbalancedMassModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6989.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

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
    ) -> "UnbalancedMassModalAnalysisAtAStiffness._Cast_UnbalancedMassModalAnalysisAtAStiffness":
        return self._Cast_UnbalancedMassModalAnalysisAtAStiffness(self)
