"""RollingRingAssemblyHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "RollingRingAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2805
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686, _5796
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyHarmonicAnalysis")


class RollingRingAssemblyHarmonicAnalysis(_5818.SpecialisedAssemblyHarmonicAnalysis):
    """RollingRingAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyHarmonicAnalysis")

    class _Cast_RollingRingAssemblyHarmonicAnalysis:
        """Special nested class for casting RollingRingAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
            parent: "RollingRingAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "RollingRingAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6954.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2805.RollingRingAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis"
    ):
        return self._Cast_RollingRingAssemblyHarmonicAnalysis(self)
