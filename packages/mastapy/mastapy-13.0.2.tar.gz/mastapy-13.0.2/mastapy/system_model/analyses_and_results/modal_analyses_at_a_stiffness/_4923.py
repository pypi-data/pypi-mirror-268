"""FlexiblePinAssemblyModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4965,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "FlexiblePinAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6897
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyModalAnalysisAtAStiffness")


class FlexiblePinAssemblyModalAnalysisAtAStiffness(
    _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """FlexiblePinAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting FlexiblePinAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
            parent: "FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "FlexiblePinAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
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
        instance_to_wrap: "FlexiblePinAssemblyModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6897.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

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
    ) -> "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness":
        return self._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness(self)
