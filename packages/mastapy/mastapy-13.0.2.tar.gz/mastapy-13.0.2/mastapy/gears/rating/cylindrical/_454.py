"""AGMAScuffingResultsRow"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.rating.cylindrical import _487
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_SCUFFING_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "AGMAScuffingResultsRow"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAScuffingResultsRow",)


Self = TypeVar("Self", bound="AGMAScuffingResultsRow")


class AGMAScuffingResultsRow(_487.ScuffingResultsRow):
    """AGMAScuffingResultsRow

    This is a mastapy class.
    """

    TYPE = _AGMA_SCUFFING_RESULTS_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAScuffingResultsRow")

    class _Cast_AGMAScuffingResultsRow:
        """Special nested class for casting AGMAScuffingResultsRow to subclasses."""

        def __init__(
            self: "AGMAScuffingResultsRow._Cast_AGMAScuffingResultsRow",
            parent: "AGMAScuffingResultsRow",
        ):
            self._parent = parent

        @property
        def scuffing_results_row(
            self: "AGMAScuffingResultsRow._Cast_AGMAScuffingResultsRow",
        ) -> "_487.ScuffingResultsRow":
            return self._parent._cast(_487.ScuffingResultsRow)

        @property
        def agma_scuffing_results_row(
            self: "AGMAScuffingResultsRow._Cast_AGMAScuffingResultsRow",
        ) -> "AGMAScuffingResultsRow":
            return self._parent

        def __getattr__(
            self: "AGMAScuffingResultsRow._Cast_AGMAScuffingResultsRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAScuffingResultsRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def central_film_thickness_isothermal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentralFilmThicknessIsothermal

        if temp is None:
            return 0.0

        return temp

    @central_film_thickness_isothermal.setter
    @enforce_parameter_types
    def central_film_thickness_isothermal(self: Self, value: "float"):
        self.wrapped.CentralFilmThicknessIsothermal = (
            float(value) if value is not None else 0.0
        )

    @property
    def central_film_thickness_with_inlet_shear_heating(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentralFilmThicknessWithInletShearHeating

        if temp is None:
            return 0.0

        return temp

    @central_film_thickness_with_inlet_shear_heating.setter
    @enforce_parameter_types
    def central_film_thickness_with_inlet_shear_heating(self: Self, value: "float"):
        self.wrapped.CentralFilmThicknessWithInletShearHeating = (
            float(value) if value is not None else 0.0
        )

    @property
    def contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactTemperature

        if temp is None:
            return 0.0

        return temp

    @contact_temperature.setter
    @enforce_parameter_types
    def contact_temperature(self: Self, value: "float"):
        self.wrapped.ContactTemperature = float(value) if value is not None else 0.0

    @property
    def dimensionless_central_film_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DimensionlessCentralFilmThickness

        if temp is None:
            return 0.0

        return temp

    @dimensionless_central_film_thickness.setter
    @enforce_parameter_types
    def dimensionless_central_film_thickness(self: Self, value: "float"):
        self.wrapped.DimensionlessCentralFilmThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def flash_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlashTemperature

        if temp is None:
            return 0.0

        return temp

    @flash_temperature.setter
    @enforce_parameter_types
    def flash_temperature(self: Self, value: "float"):
        self.wrapped.FlashTemperature = float(value) if value is not None else 0.0

    @property
    def hertzian_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HertzianStress

        if temp is None:
            return 0.0

        return temp

    @hertzian_stress.setter
    @enforce_parameter_types
    def hertzian_stress(self: Self, value: "float"):
        self.wrapped.HertzianStress = float(value) if value is not None else 0.0

    @property
    def load_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadParameter

        if temp is None:
            return 0.0

        return temp

    @load_parameter.setter
    @enforce_parameter_types
    def load_parameter(self: Self, value: "float"):
        self.wrapped.LoadParameter = float(value) if value is not None else 0.0

    @property
    def mean_coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @mean_coefficient_of_friction.setter
    @enforce_parameter_types
    def mean_coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.MeanCoefficientOfFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @pinion_rolling_velocity.setter
    @enforce_parameter_types
    def pinion_rolling_velocity(self: Self, value: "float"):
        self.wrapped.PinionRollingVelocity = float(value) if value is not None else 0.0

    @property
    def semi_width_of_hertzian_contact_band(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SemiWidthOfHertzianContactBand

        if temp is None:
            return 0.0

        return temp

    @semi_width_of_hertzian_contact_band.setter
    @enforce_parameter_types
    def semi_width_of_hertzian_contact_band(self: Self, value: "float"):
        self.wrapped.SemiWidthOfHertzianContactBand = (
            float(value) if value is not None else 0.0
        )

    @property
    def slideto_roll_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidetoRollRatio

        if temp is None:
            return 0.0

        return temp

    @slideto_roll_ratio.setter
    @enforce_parameter_types
    def slideto_roll_ratio(self: Self, value: "float"):
        self.wrapped.SlidetoRollRatio = float(value) if value is not None else 0.0

    @property
    def sliding_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @sliding_velocity.setter
    @enforce_parameter_types
    def sliding_velocity(self: Self, value: "float"):
        self.wrapped.SlidingVelocity = float(value) if value is not None else 0.0

    @property
    def specific_film_thickness_with_filter_cutoff_wavelength_isothermal(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.SpecificFilmThicknessWithFilterCutoffWavelengthIsothermal

        if temp is None:
            return 0.0

        return temp

    @specific_film_thickness_with_filter_cutoff_wavelength_isothermal.setter
    @enforce_parameter_types
    def specific_film_thickness_with_filter_cutoff_wavelength_isothermal(
        self: Self, value: "float"
    ):
        self.wrapped.SpecificFilmThicknessWithFilterCutoffWavelengthIsothermal = (
            float(value) if value is not None else 0.0
        )

    @property
    def specific_film_thickness_with_filter_cutoff_wavelength_with_inlet_shear_heating(
        self: Self,
    ) -> "float":
        """float"""
        temp = (
            self.wrapped.SpecificFilmThicknessWithFilterCutoffWavelengthWithInletShearHeating
        )

        if temp is None:
            return 0.0

        return temp

    @specific_film_thickness_with_filter_cutoff_wavelength_with_inlet_shear_heating.setter
    @enforce_parameter_types
    def specific_film_thickness_with_filter_cutoff_wavelength_with_inlet_shear_heating(
        self: Self, value: "float"
    ):
        self.wrapped.SpecificFilmThicknessWithFilterCutoffWavelengthWithInletShearHeating = (
            float(value) if value is not None else 0.0
        )

    @property
    def speed_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpeedParameter

        if temp is None:
            return 0.0

        return temp

    @speed_parameter.setter
    @enforce_parameter_types
    def speed_parameter(self: Self, value: "float"):
        self.wrapped.SpeedParameter = float(value) if value is not None else 0.0

    @property
    def thermal_loading_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThermalLoadingParameter

        if temp is None:
            return 0.0

        return temp

    @thermal_loading_parameter.setter
    @enforce_parameter_types
    def thermal_loading_parameter(self: Self, value: "float"):
        self.wrapped.ThermalLoadingParameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def thermal_reduction_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThermalReductionFactor

        if temp is None:
            return 0.0

        return temp

    @thermal_reduction_factor.setter
    @enforce_parameter_types
    def thermal_reduction_factor(self: Self, value: "float"):
        self.wrapped.ThermalReductionFactor = float(value) if value is not None else 0.0

    @property
    def wheel_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @wheel_rolling_velocity.setter
    @enforce_parameter_types
    def wheel_rolling_velocity(self: Self, value: "float"):
        self.wrapped.WheelRollingVelocity = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "AGMAScuffingResultsRow._Cast_AGMAScuffingResultsRow":
        return self._Cast_AGMAScuffingResultsRow(self)
