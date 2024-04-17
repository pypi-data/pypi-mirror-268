"""RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6154,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6112,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6147,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation")


class RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6154.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6147,
            )

            return self._parent._cast(
                _6147.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6112.RootAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RootAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6112.RootAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RootAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation(self)
