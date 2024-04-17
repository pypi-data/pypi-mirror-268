"""FlexiblePinAssemblyCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundHarmonicAnalysis")


class FlexiblePinAssemblyCompoundHarmonicAnalysis(
    _5985.SpecialisedAssemblyCompoundHarmonicAnalysis
):
    """FlexiblePinAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
            parent: "FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
        ) -> "FlexiblePinAssemblyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_5759.FlexiblePinAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis]

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
    ) -> "List[_5759.FlexiblePinAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis]

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
    ) -> "FlexiblePinAssemblyCompoundHarmonicAnalysis._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis":
        return self._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysis(self)
