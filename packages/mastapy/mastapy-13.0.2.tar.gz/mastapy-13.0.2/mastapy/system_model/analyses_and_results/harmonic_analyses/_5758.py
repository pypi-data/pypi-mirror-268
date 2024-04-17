"""FEPartHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
from mastapy.system_model.analyses_and_results import _2662
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "FEPartHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.modal_analyses import _4640
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5772,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5865,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2765
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartHarmonicAnalysis",)


Self = TypeVar("Self", bound="FEPartHarmonicAnalysis")


class FEPartHarmonicAnalysis(
    _5689.AbstractShaftOrHousingHarmonicAnalysis,
    _2662.IHaveFEPartHarmonicAnalysisResults,
):
    """FEPartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartHarmonicAnalysis")

    class _Cast_FEPartHarmonicAnalysis:
        """Special nested class for casting FEPartHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
            parent: "FEPartHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_5689.AbstractShaftOrHousingHarmonicAnalysis":
            return self._parent._cast(_5689.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis",
        ) -> "FEPartHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def export_accelerations(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExportAccelerations

        if temp is None:
            return ""

        return temp

    @property
    def export_displacements(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExportDisplacements

        if temp is None:
            return ""

        return temp

    @property
    def export_forces(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExportForces

        if temp is None:
            return ""

        return temp

    @property
    def export_velocities(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExportVelocities

        if temp is None:
            return ""

        return temp

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4640.FEPartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def export(self: Self) -> "_5772.HarmonicAnalysisFEExportOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisFEExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(self: Self) -> "_5865.FEPartHarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.FEPartHarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2765.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FEPartHarmonicAnalysis._Cast_FEPartHarmonicAnalysis":
        return self._Cast_FEPartHarmonicAnalysis(self)
