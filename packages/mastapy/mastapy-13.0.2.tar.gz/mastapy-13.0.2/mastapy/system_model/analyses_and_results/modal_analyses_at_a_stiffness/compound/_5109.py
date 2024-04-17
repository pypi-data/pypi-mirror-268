"""SynchroniserCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5094,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4981,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4996,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserCompoundModalAnalysisAtAStiffness")


class SynchroniserCompoundModalAnalysisAtAStiffness(
    _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
):
    """SynchroniserCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
            parent: "SynchroniserCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5094.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
        ) -> "SynchroniserCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SynchroniserCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2610.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4981.SynchroniserModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserModalAnalysisAtAStiffness]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4981.SynchroniserModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserCompoundModalAnalysisAtAStiffness._Cast_SynchroniserCompoundModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserCompoundModalAnalysisAtAStiffness(self)
