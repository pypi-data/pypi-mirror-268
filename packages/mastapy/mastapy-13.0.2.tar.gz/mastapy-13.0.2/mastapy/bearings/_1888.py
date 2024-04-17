"""BearingSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.bearings import _1891
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingSettingsItem"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1897, _1890


__docformat__ = "restructuredtext en"
__all__ = ("BearingSettingsItem",)


Self = TypeVar("Self", bound="BearingSettingsItem")


class BearingSettingsItem(_1836.NamedDatabaseItem):
    """BearingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingSettingsItem")

    class _Cast_BearingSettingsItem:
        """Special nested class for casting BearingSettingsItem to subclasses."""

        def __init__(
            self: "BearingSettingsItem._Cast_BearingSettingsItem",
            parent: "BearingSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "BearingSettingsItem._Cast_BearingSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bearing_settings_item(
            self: "BearingSettingsItem._Cast_BearingSettingsItem",
        ) -> "BearingSettingsItem":
            return self._parent

        def __getattr__(
            self: "BearingSettingsItem._Cast_BearingSettingsItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingSettingsItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_bearing_weibull_reliability_slope(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BallBearingWeibullReliabilitySlope

        if temp is None:
            return 0.0

        return temp

    @ball_bearing_weibull_reliability_slope.setter
    @enforce_parameter_types
    def ball_bearing_weibull_reliability_slope(self: Self, value: "float"):
        self.wrapped.BallBearingWeibullReliabilitySlope = (
            float(value) if value is not None else 0.0
        )

    @property
    def failure_probability_for_rating_life_percent(self: Self) -> "_1897.RatingLife":
        """mastapy.bearings.RatingLife"""
        temp = self.wrapped.FailureProbabilityForRatingLifePercent

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bearings.RatingLife")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.bearings._1897", "RatingLife")(
            value
        )

    @failure_probability_for_rating_life_percent.setter
    @enforce_parameter_types
    def failure_probability_for_rating_life_percent(
        self: Self, value: "_1897.RatingLife"
    ):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bearings.RatingLife")
        self.wrapped.FailureProbabilityForRatingLifePercent = value

    @property
    def include_exponent_and_reduction_factors_in_isots162812008(
        self: Self,
    ) -> "_1890.ExponentAndReductionFactorsInISO16281Calculation":
        """mastapy.bearings.ExponentAndReductionFactorsInISO16281Calculation"""
        temp = self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.ExponentAndReductionFactorsInISO16281Calculation",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1890", "ExponentAndReductionFactorsInISO16281Calculation"
        )(value)

    @include_exponent_and_reduction_factors_in_isots162812008.setter
    @enforce_parameter_types
    def include_exponent_and_reduction_factors_in_isots162812008(
        self: Self, value: "_1890.ExponentAndReductionFactorsInISO16281Calculation"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.ExponentAndReductionFactorsInISO16281Calculation",
        )
        self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008 = value

    @property
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions":
        """EnumWithSelectedValue[mastapy.bearings.FluidFilmTemperatureOptions]"""
        temp = (
            self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings
        )

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings.setter
    @enforce_parameter_types
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(
        self: Self, value: "_1891.FluidFilmTemperatureOptions"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings = (
            value
        )

    @property
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions":
        """EnumWithSelectedValue[mastapy.bearings.FluidFilmTemperatureOptions]"""
        temp = self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lubricant_film_temperature_calculation_splashed_submerged_bearings.setter
    @enforce_parameter_types
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(
        self: Self, value: "_1891.FluidFilmTemperatureOptions"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings = (
            value
        )

    @property
    def number_of_strips_for_roller_calculation(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfStripsForRollerCalculation

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_strips_for_roller_calculation.setter
    @enforce_parameter_types
    def number_of_strips_for_roller_calculation(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def roller_bearing_weibull_reliability_slope(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollerBearingWeibullReliabilitySlope

        if temp is None:
            return 0.0

        return temp

    @roller_bearing_weibull_reliability_slope.setter
    @enforce_parameter_types
    def roller_bearing_weibull_reliability_slope(self: Self, value: "float"):
        self.wrapped.RollerBearingWeibullReliabilitySlope = (
            float(value) if value is not None else 0.0
        )

    @property
    def third_weibull_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThirdWeibullParameter

        if temp is None:
            return 0.0

        return temp

    @third_weibull_parameter.setter
    @enforce_parameter_types
    def third_weibull_parameter(self: Self, value: "float"):
        self.wrapped.ThirdWeibullParameter = float(value) if value is not None else 0.0

    @property
    def tolerance_used_for_diameter_warnings_and_database_filter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter

        if temp is None:
            return 0.0

        return temp

    @tolerance_used_for_diameter_warnings_and_database_filter.setter
    @enforce_parameter_types
    def tolerance_used_for_diameter_warnings_and_database_filter(
        self: Self, value: "float"
    ):
        self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_plain_journal_bearing_misalignment_factors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UsePlainJournalBearingMisalignmentFactors

        if temp is None:
            return False

        return temp

    @use_plain_journal_bearing_misalignment_factors.setter
    @enforce_parameter_types
    def use_plain_journal_bearing_misalignment_factors(self: Self, value: "bool"):
        self.wrapped.UsePlainJournalBearingMisalignmentFactors = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "BearingSettingsItem._Cast_BearingSettingsItem":
        return self._Cast_BearingSettingsItem(self)
