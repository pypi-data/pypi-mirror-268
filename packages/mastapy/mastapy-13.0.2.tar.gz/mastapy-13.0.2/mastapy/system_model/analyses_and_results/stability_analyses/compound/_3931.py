"""ConceptCouplingCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConceptCouplingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.stability_analyses import _3799
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4003,
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundStabilityAnalysis")


class ConceptCouplingCompoundStabilityAnalysis(_3942.CouplingCompoundStabilityAnalysis):
    """ConceptCouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundStabilityAnalysis"
    )

    class _Cast_ConceptCouplingCompoundStabilityAnalysis:
        """Special nested class for casting ConceptCouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
            parent: "ConceptCouplingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_3942.CouplingCompoundStabilityAnalysis":
            return self._parent._cast(_3942.CouplingCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "ConceptCouplingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

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
    ) -> "List[_3799.ConceptCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingStabilityAnalysis]

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
    ) -> "List[_3799.ConceptCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingStabilityAnalysis]

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
    ) -> "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis":
        return self._Cast_ConceptCouplingCompoundStabilityAnalysis(self)
