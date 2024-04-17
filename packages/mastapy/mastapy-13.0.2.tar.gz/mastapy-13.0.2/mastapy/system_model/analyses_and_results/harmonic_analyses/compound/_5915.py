"""ConceptCouplingHalfCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundHarmonicAnalysis")


class ConceptCouplingHalfCompoundHarmonicAnalysis(
    _5926.CouplingHalfCompoundHarmonicAnalysis
):
    """ConceptCouplingHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundHarmonicAnalysis"
    )

    class _Cast_ConceptCouplingHalfCompoundHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
            parent: "ConceptCouplingHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5926.CouplingHalfCompoundHarmonicAnalysis":
            return self._parent._cast(_5926.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
        ) -> "ConceptCouplingHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingHalfCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5715.ConceptCouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5715.ConceptCouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfCompoundHarmonicAnalysis._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis":
        return self._Cast_ConceptCouplingHalfCompoundHarmonicAnalysis(self)
