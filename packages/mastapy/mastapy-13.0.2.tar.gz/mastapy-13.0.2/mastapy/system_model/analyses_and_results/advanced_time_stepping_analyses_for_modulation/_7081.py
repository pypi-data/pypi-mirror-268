"""HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OPTIONS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
)


class HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation(
    _5774.HarmonicAnalysisOptions
):
    """HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_OPTIONS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
            parent: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_options(
            self: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_5774.HarmonicAnalysisOptions":
            return self._parent._cast(_5774.HarmonicAnalysisOptions)

        @property
        def harmonic_analysis_options_for_advanced_time_stepping_analysis_for_modulation(
            self: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_uncoupled_modes_during_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateUncoupledModesDuringAnalysis

        if temp is None:
            return False

        return temp

    @calculate_uncoupled_modes_during_analysis.setter
    @enforce_parameter_types
    def calculate_uncoupled_modes_during_analysis(self: Self, value: "bool"):
        self.wrapped.CalculateUncoupledModesDuringAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def crop_to_speed_range_for_export_and_reports(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CropToSpeedRangeForExportAndReports

        if temp is None:
            return False

        return temp

    @crop_to_speed_range_for_export_and_reports.setter
    @enforce_parameter_types
    def crop_to_speed_range_for_export_and_reports(self: Self, value: "bool"):
        self.wrapped.CropToSpeedRangeForExportAndReports = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation(
            self
        )
