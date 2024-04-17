"""HarmonicAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5807,
        _5760,
        _5819,
        _5826,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
        _5855,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4665
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7081,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisOptions",)


Self = TypeVar("Self", bound="HarmonicAnalysisOptions")


class HarmonicAnalysisOptions(_0.APIBase):
    """HarmonicAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisOptions")

    class _Cast_HarmonicAnalysisOptions:
        """Special nested class for casting HarmonicAnalysisOptions to subclasses."""

        def __init__(
            self: "HarmonicAnalysisOptions._Cast_HarmonicAnalysisOptions",
            parent: "HarmonicAnalysisOptions",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_options_for_advanced_time_stepping_analysis_for_modulation(
            self: "HarmonicAnalysisOptions._Cast_HarmonicAnalysisOptions",
        ) -> (
            "_7081.HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_options(
            self: "HarmonicAnalysisOptions._Cast_HarmonicAnalysisOptions",
        ) -> "HarmonicAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisOptions._Cast_HarmonicAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def amplitude_cut_off_for_linear_te(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AmplitudeCutOffForLinearTE

        if temp is None:
            return 0.0

        return temp

    @amplitude_cut_off_for_linear_te.setter
    @enforce_parameter_types
    def amplitude_cut_off_for_linear_te(self: Self, value: "float"):
        self.wrapped.AmplitudeCutOffForLinearTE = (
            float(value) if value is not None else 0.0
        )

    @property
    def amplitude_cut_off_for_misalignment_excitation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AmplitudeCutOffForMisalignmentExcitation

        if temp is None:
            return 0.0

        return temp

    @amplitude_cut_off_for_misalignment_excitation.setter
    @enforce_parameter_types
    def amplitude_cut_off_for_misalignment_excitation(self: Self, value: "float"):
        self.wrapped.AmplitudeCutOffForMisalignmentExcitation = (
            float(value) if value is not None else 0.0
        )

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
    def modal_damping_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModalDampingFactor

        if temp is None:
            return 0.0

        return temp

    @modal_damping_factor.setter
    @enforce_parameter_types
    def modal_damping_factor(self: Self, value: "float"):
        self.wrapped.ModalDampingFactor = float(value) if value is not None else 0.0

    @property
    def number_of_harmonics(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfHarmonics

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_harmonics.setter
    @enforce_parameter_types
    def number_of_harmonics(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfHarmonics = value

    @property
    def penalty_mass_for_enforced_te(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PenaltyMassForEnforcedTE

        if temp is None:
            return 0.0

        return temp

    @penalty_mass_for_enforced_te.setter
    @enforce_parameter_types
    def penalty_mass_for_enforced_te(self: Self, value: "float"):
        self.wrapped.PenaltyMassForEnforcedTE = (
            float(value) if value is not None else 0.0
        )

    @property
    def penalty_stiffness_for_enforced_te(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PenaltyStiffnessForEnforcedTE

        if temp is None:
            return 0.0

        return temp

    @penalty_stiffness_for_enforced_te.setter
    @enforce_parameter_types
    def penalty_stiffness_for_enforced_te(self: Self, value: "float"):
        self.wrapped.PenaltyStiffnessForEnforcedTE = (
            float(value) if value is not None else 0.0
        )

    @property
    def rayleigh_damping_alpha(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return temp

    @rayleigh_damping_alpha.setter
    @enforce_parameter_types
    def rayleigh_damping_alpha(self: Self, value: "float"):
        self.wrapped.RayleighDampingAlpha = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return temp

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "float"):
        self.wrapped.RayleighDampingBeta = float(value) if value is not None else 0.0

    @property
    def response_cache_level(self: Self) -> "_5807.ResponseCacheLevel":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ResponseCacheLevel"""
        temp = self.wrapped.ResponseCacheLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ResponseCacheLevel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.harmonic_analyses._5807",
            "ResponseCacheLevel",
        )(value)

    @response_cache_level.setter
    @enforce_parameter_types
    def response_cache_level(self: Self, value: "_5807.ResponseCacheLevel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ResponseCacheLevel",
        )
        self.wrapped.ResponseCacheLevel = value

    @property
    def specify_per_mode_damping_factors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyPerModeDampingFactors

        if temp is None:
            return False

        return temp

    @specify_per_mode_damping_factors.setter
    @enforce_parameter_types
    def specify_per_mode_damping_factors(self: Self, value: "bool"):
        self.wrapped.SpecifyPerModeDampingFactors = (
            bool(value) if value is not None else False
        )

    @property
    def update_dynamic_response_chart_on_change_of_settings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UpdateDynamicResponseChartOnChangeOfSettings

        if temp is None:
            return False

        return temp

    @update_dynamic_response_chart_on_change_of_settings.setter
    @enforce_parameter_types
    def update_dynamic_response_chart_on_change_of_settings(self: Self, value: "bool"):
        self.wrapped.UpdateDynamicResponseChartOnChangeOfSettings = (
            bool(value) if value is not None else False
        )

    @property
    def excitation_selection(self: Self) -> "_5855.ExcitationSourceSelectionGroup":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ExcitationSourceSelectionGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frequency_options(
        self: Self,
    ) -> "_5760.FrequencyOptionsForHarmonicAnalysisResults":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FrequencyOptionsForHarmonicAnalysisResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_options(self: Self) -> "_4665.ModalAnalysisOptions":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reference_speed_options(
        self: Self,
    ) -> "_5819.SpeedOptionsForHarmonicAnalysisResults":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpeedOptionsForHarmonicAnalysisResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceSpeedOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_options(self: Self) -> "_5826.StiffnessOptionsForHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StiffnessOptionsForHarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def per_mode_damping_factors(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PerModeDampingFactors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def set_per_mode_damping_factor(self: Self, mode: "int", damping: "float"):
        """Method does not return.

        Args:
            mode (int)
            damping (float)
        """
        mode = int(mode)
        damping = float(damping)
        self.wrapped.SetPerModeDampingFactor(
            mode if mode else 0, damping if damping else 0.0
        )

    @enforce_parameter_types
    def set_per_mode_damping_factors(self: Self, damping_values: "List[float]"):
        """Method does not return.

        Args:
            damping_values (List[float])
        """
        damping_values = conversion.mp_to_pn_list_float(damping_values)
        self.wrapped.SetPerModeDampingFactors(damping_values)

    @property
    def cast_to(self: Self) -> "HarmonicAnalysisOptions._Cast_HarmonicAnalysisOptions":
        return self._Cast_HarmonicAnalysisOptions(self)
