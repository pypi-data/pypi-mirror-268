"""FEPartAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7016,
)
from mastapy.system_model.analyses_and_results import _2662
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5772
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5865,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2765
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="FEPartAdvancedTimeSteppingAnalysisForModulation")


class FEPartAdvancedTimeSteppingAnalysisForModulation(
    _7016.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation,
    _2662.IHaveFEPartHarmonicAnalysisResults,
):
    """FEPartAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FE_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_FEPartAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FEPartAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
            parent: "FEPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7016.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7016.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "FEPartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "FEPartAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
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
    def planetaries(
        self: Self,
    ) -> "List[FEPartAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.FEPartAdvancedTimeSteppingAnalysisForModulation]

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
    def cast_to(
        self: Self,
    ) -> "FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation(self)
