"""RootAssemblyCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "RootAssemblyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5813
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundHarmonicAnalysis")


class RootAssemblyCompoundHarmonicAnalysis(_5894.AssemblyCompoundHarmonicAnalysis):
    """RootAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyCompoundHarmonicAnalysis")

    class _Cast_RootAssemblyCompoundHarmonicAnalysis:
        """Special nested class for casting RootAssemblyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
            parent: "RootAssemblyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_harmonic_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_5894.AssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5894.AssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
        ) -> "RootAssemblyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5813.RootAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis]

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
    ) -> "List[_5813.RootAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis]

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
    ) -> "RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis":
        return self._Cast_RootAssemblyCompoundHarmonicAnalysis(self)
