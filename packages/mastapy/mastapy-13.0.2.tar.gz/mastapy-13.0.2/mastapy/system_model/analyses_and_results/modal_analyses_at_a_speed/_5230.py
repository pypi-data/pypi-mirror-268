"""SpringDamperModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5164
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5224,
        _5125,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperModalAnalysisAtASpeed")


class SpringDamperModalAnalysisAtASpeed(_5164.CouplingModalAnalysisAtASpeed):
    """SpringDamperModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperModalAnalysisAtASpeed")

    class _Cast_SpringDamperModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
            parent: "SpringDamperModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_5164.CouplingModalAnalysisAtASpeed":
            return self._parent._cast(_5164.CouplingModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_5224.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_5125.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
        ) -> "SpringDamperModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SpringDamperModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6967.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

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
    ) -> "SpringDamperModalAnalysisAtASpeed._Cast_SpringDamperModalAnalysisAtASpeed":
        return self._Cast_SpringDamperModalAnalysisAtASpeed(self)
