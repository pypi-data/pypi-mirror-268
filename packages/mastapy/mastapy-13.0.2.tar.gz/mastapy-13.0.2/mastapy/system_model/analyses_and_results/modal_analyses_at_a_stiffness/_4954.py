"""PowerLoadModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4989,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PowerLoadModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4944,
        _4890,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PowerLoadModalAnalysisAtAStiffness")


class PowerLoadModalAnalysisAtAStiffness(
    _4989.VirtualComponentModalAnalysisAtAStiffness
):
    """PowerLoadModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadModalAnalysisAtAStiffness")

    class _Cast_PowerLoadModalAnalysisAtAStiffness:
        """Special nested class for casting PowerLoadModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
            parent: "PowerLoadModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_4989.VirtualComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4989.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_4944.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
        ) -> "PowerLoadModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PowerLoadModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadModalAnalysisAtAStiffness._Cast_PowerLoadModalAnalysisAtAStiffness":
        return self._Cast_PowerLoadModalAnalysisAtAStiffness(self)
