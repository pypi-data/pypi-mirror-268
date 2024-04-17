"""CouplingCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5094,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4904,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5017,
        _5022,
        _5076,
        _5098,
        _5113,
        _4996,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingCompoundModalAnalysisAtAStiffness")


class CouplingCompoundModalAnalysisAtAStiffness(
    _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
):
    """CouplingCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
            parent: "CouplingCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5017.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(_5017.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(
                _5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "CouplingCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4904.CouplingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4904.CouplingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness":
        return self._Cast_CouplingCompoundModalAnalysisAtAStiffness(self)
