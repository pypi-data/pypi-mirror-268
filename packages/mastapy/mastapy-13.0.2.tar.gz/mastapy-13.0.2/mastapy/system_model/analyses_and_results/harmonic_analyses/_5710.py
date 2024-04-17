"""ClutchHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ClutchHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2585
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.system_deflections import _2721
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5818,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHarmonicAnalysis",)


Self = TypeVar("Self", bound="ClutchHarmonicAnalysis")


class ClutchHarmonicAnalysis(_5727.CouplingHarmonicAnalysis):
    """ClutchHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHarmonicAnalysis")

    class _Cast_ClutchHarmonicAnalysis:
        """Special nested class for casting ClutchHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
            parent: "ClutchHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_5727.CouplingHarmonicAnalysis":
            return self._parent._cast(_5727.CouplingHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis",
        ) -> "ClutchHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2585.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2721.ClutchSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchHarmonicAnalysis._Cast_ClutchHarmonicAnalysis":
        return self._Cast_ClutchHarmonicAnalysis(self)
