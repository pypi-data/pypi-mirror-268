"""SpringDamperCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpringDamperCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.modal_analyses import _4696
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4834,
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperCompoundModalAnalysis")


class SpringDamperCompoundModalAnalysis(_4773.CouplingCompoundModalAnalysis):
    """SpringDamperCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperCompoundModalAnalysis")

    class _Cast_SpringDamperCompoundModalAnalysis:
        """Special nested class for casting SpringDamperCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
            parent: "SpringDamperCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_4773.CouplingCompoundModalAnalysis":
            return self._parent._cast(_4773.CouplingCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
        ) -> "SpringDamperCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4696.SpringDamperModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_4696.SpringDamperModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis]

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
    ) -> "SpringDamperCompoundModalAnalysis._Cast_SpringDamperCompoundModalAnalysis":
        return self._Cast_SpringDamperCompoundModalAnalysis(self)
