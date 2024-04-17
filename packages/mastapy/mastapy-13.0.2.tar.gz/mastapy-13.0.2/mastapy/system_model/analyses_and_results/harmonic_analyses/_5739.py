"""DatumHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "DatumHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6878
    from mastapy.system_model.analyses_and_results.system_deflections import _2759
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("DatumHarmonicAnalysis",)


Self = TypeVar("Self", bound="DatumHarmonicAnalysis")


class DatumHarmonicAnalysis(_5713.ComponentHarmonicAnalysis):
    """DatumHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumHarmonicAnalysis")

    class _Cast_DatumHarmonicAnalysis:
        """Special nested class for casting DatumHarmonicAnalysis to subclasses."""

        def __init__(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
            parent: "DatumHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "DatumHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6878.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2759.DatumSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis":
        return self._Cast_DatumHarmonicAnalysis(self)
