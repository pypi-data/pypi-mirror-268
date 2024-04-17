"""CouplingModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5148,
        _5153,
        _5208,
        _5230,
        _5244,
        _5125,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingModalAnalysisAtASpeed")


class CouplingModalAnalysisAtASpeed(_5224.SpecialisedAssemblyModalAnalysisAtASpeed):
    """CouplingModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysisAtASpeed")

    class _Cast_CouplingModalAnalysisAtASpeed:
        """Special nested class for casting CouplingModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
            parent: "CouplingModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5224.SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5224.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5125.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5148.ClutchModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ClutchModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5153.ConceptCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5208.PartToPartShearCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5230.SpringDamperModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SpringDamperModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "_5244.TorqueConverterModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.TorqueConverterModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "CouplingModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed":
        return self._Cast_CouplingModalAnalysisAtASpeed(self)
