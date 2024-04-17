"""PartToPartShearCouplingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4904,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PartToPartShearCouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4965,
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PartToPartShearCouplingModalAnalysisAtAStiffness")


class PartToPartShearCouplingModalAnalysisAtAStiffness(
    _4904.CouplingModalAnalysisAtAStiffness
):
    """PartToPartShearCouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingModalAnalysisAtAStiffness"
    )

    class _Cast_PartToPartShearCouplingModalAnalysisAtAStiffness:
        """Special nested class for casting PartToPartShearCouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
            parent: "PartToPartShearCouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4904.CouplingModalAnalysisAtAStiffness":
            return self._parent._cast(_4904.CouplingModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PartToPartShearCouplingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6940.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness":
        return self._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness(self)
