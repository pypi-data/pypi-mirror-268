"""CouplingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4965,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4888,
        _4893,
        _4949,
        _4971,
        _4985,
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingModalAnalysisAtAStiffness")


class CouplingModalAnalysisAtAStiffness(
    _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """CouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysisAtAStiffness")

    class _Cast_CouplingModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
            parent: "CouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4888.ClutchModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ClutchModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4893.ConceptCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(_4893.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4949.PartToPartShearCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4971.SpringDamperModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.SpringDamperModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4985.TorqueConverterModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "CouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingModalAnalysisAtAStiffness.TYPE"
    ):
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
    ) -> "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness":
        return self._Cast_CouplingModalAnalysisAtAStiffness(self)
