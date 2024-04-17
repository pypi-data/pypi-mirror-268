"""CycloidalAssemblyCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CycloidalAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2575
    from mastapy.system_model.analyses_and_results.modal_analyses import _4624
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalAssemblyCompoundModalAnalysis")


class CycloidalAssemblyCompoundModalAnalysis(
    _4834.SpecialisedAssemblyCompoundModalAnalysis
):
    """CycloidalAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalAssemblyCompoundModalAnalysis"
    )

    class _Cast_CycloidalAssemblyCompoundModalAnalysis:
        """Special nested class for casting CycloidalAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
            parent: "CycloidalAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
        ) -> "CycloidalAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

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
    ) -> "List[_4624.CycloidalAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalAssemblyModalAnalysis]

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
    ) -> "List[_4624.CycloidalAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalAssemblyModalAnalysis]

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
    ) -> "CycloidalAssemblyCompoundModalAnalysis._Cast_CycloidalAssemblyCompoundModalAnalysis":
        return self._Cast_CycloidalAssemblyCompoundModalAnalysis(self)
