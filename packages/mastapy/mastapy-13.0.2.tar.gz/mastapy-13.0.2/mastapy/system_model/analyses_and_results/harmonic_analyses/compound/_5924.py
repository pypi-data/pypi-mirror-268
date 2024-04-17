"""CouplingCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CouplingCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5908,
        _5913,
        _5967,
        _5989,
        _6004,
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundHarmonicAnalysis")


class CouplingCompoundHarmonicAnalysis(
    _5985.SpecialisedAssemblyCompoundHarmonicAnalysis
):
    """CouplingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundHarmonicAnalysis")

    class _Cast_CouplingCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
            parent: "CouplingCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5908.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ClutchCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5913.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5967.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(
                _5967.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5989.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.SpringDamperCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_6004.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "CouplingCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_5727.CouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis]

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
    ) -> "List[_5727.CouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis]

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
    ) -> "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis":
        return self._Cast_CouplingCompoundHarmonicAnalysis(self)
