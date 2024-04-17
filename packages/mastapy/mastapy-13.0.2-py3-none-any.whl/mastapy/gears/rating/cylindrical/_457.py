"""CylindricalGearDesignAndRatingSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import (
    constructor,
    conversion,
    overridable_enum_runtime,
    enum_with_selected_value_runtime,
)
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy.gears import _337
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials import _254
from mastapy.gears.rating.cylindrical import _484, _485
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical",
    "CylindricalGearDesignAndRatingSettingsItem",
)

if TYPE_CHECKING:
    from mastapy.gears import _347, _318
    from mastapy.gears.rating.cylindrical import (
        _490,
        _475,
        _486,
        _476,
        _479,
        _482,
        _489,
    )
    from mastapy.gears.gear_designs.cylindrical import _1030
    from mastapy.utility.units_and_measurements import _1614


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignAndRatingSettingsItem",)


Self = TypeVar("Self", bound="CylindricalGearDesignAndRatingSettingsItem")


class CylindricalGearDesignAndRatingSettingsItem(_1836.NamedDatabaseItem):
    """CylindricalGearDesignAndRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_ITEM
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearDesignAndRatingSettingsItem"
    )

    class _Cast_CylindricalGearDesignAndRatingSettingsItem:
        """Special nested class for casting CylindricalGearDesignAndRatingSettingsItem to subclasses."""

        def __init__(
            self: "CylindricalGearDesignAndRatingSettingsItem._Cast_CylindricalGearDesignAndRatingSettingsItem",
            parent: "CylindricalGearDesignAndRatingSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "CylindricalGearDesignAndRatingSettingsItem._Cast_CylindricalGearDesignAndRatingSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_design_and_rating_settings_item(
            self: "CylindricalGearDesignAndRatingSettingsItem._Cast_CylindricalGearDesignAndRatingSettingsItem",
        ) -> "CylindricalGearDesignAndRatingSettingsItem":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignAndRatingSettingsItem._Cast_CylindricalGearDesignAndRatingSettingsItem",
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
        self: Self, instance_to_wrap: "CylindricalGearDesignAndRatingSettingsItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma_quality_grade_type(self: Self) -> "_347.QualityGradeTypes":
        """mastapy.gears.QualityGradeTypes"""
        temp = self.wrapped.AGMAQualityGradeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.QualityGradeTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._347", "QualityGradeTypes")(
            value
        )

    @agma_quality_grade_type.setter
    @enforce_parameter_types
    def agma_quality_grade_type(self: Self, value: "_347.QualityGradeTypes"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.QualityGradeTypes")
        self.wrapped.AGMAQualityGradeType = value

    @property
    def agma_stress_cycle_factor_influence_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AGMAStressCycleFactorInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @agma_stress_cycle_factor_influence_factor.setter
    @enforce_parameter_types
    def agma_stress_cycle_factor_influence_factor(self: Self, value: "float"):
        self.wrapped.AGMAStressCycleFactorInfluenceFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def agma_tolerances_standard(self: Self) -> "_318.AGMAToleranceStandard":
        """mastapy.gears.AGMAToleranceStandard"""
        temp = self.wrapped.AGMATolerancesStandard

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.AGMAToleranceStandard"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._318", "AGMAToleranceStandard"
        )(value)

    @agma_tolerances_standard.setter
    @enforce_parameter_types
    def agma_tolerances_standard(self: Self, value: "_318.AGMAToleranceStandard"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.AGMAToleranceStandard"
        )
        self.wrapped.AGMATolerancesStandard = value

    @property
    def allow_transverse_contact_ratio_less_than_one(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AllowTransverseContactRatioLessThanOne

        if temp is None:
            return False

        return temp

    @allow_transverse_contact_ratio_less_than_one.setter
    @enforce_parameter_types
    def allow_transverse_contact_ratio_less_than_one(self: Self, value: "bool"):
        self.wrapped.AllowTransverseContactRatioLessThanOne = (
            bool(value) if value is not None else False
        )

    @property
    def always_use_chosen_tooth_thickness_for_bending_strength(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AlwaysUseChosenToothThicknessForBendingStrength

        if temp is None:
            return False

        return temp

    @always_use_chosen_tooth_thickness_for_bending_strength.setter
    @enforce_parameter_types
    def always_use_chosen_tooth_thickness_for_bending_strength(
        self: Self, value: "bool"
    ):
        self.wrapped.AlwaysUseChosenToothThicknessForBendingStrength = (
            bool(value) if value is not None else False
        )

    @property
    def apply_application_and_dynamic_factor_by_default(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyApplicationAndDynamicFactorByDefault

        if temp is None:
            return False

        return temp

    @apply_application_and_dynamic_factor_by_default.setter
    @enforce_parameter_types
    def apply_application_and_dynamic_factor_by_default(self: Self, value: "bool"):
        self.wrapped.ApplyApplicationAndDynamicFactorByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.ApplyWorkHardeningFactorForWroughtNormalisedLowCarbonSteelAndCastSteel
        )

        if temp is None:
            return False

        return temp

    @apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel.setter
    @enforce_parameter_types
    def apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel(
        self: Self, value: "bool"
    ):
        self.wrapped.ApplyWorkHardeningFactorForWroughtNormalisedLowCarbonSteelAndCastSteel = (
            bool(value) if value is not None else False
        )

    @property
    def chosen_tooth_thickness_for_bending_strength(
        self: Self,
    ) -> "_490.ToothThicknesses":
        """mastapy.gears.rating.cylindrical.ToothThicknesses"""
        temp = self.wrapped.ChosenToothThicknessForBendingStrength

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.ToothThicknesses"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._490", "ToothThicknesses"
        )(value)

    @chosen_tooth_thickness_for_bending_strength.setter
    @enforce_parameter_types
    def chosen_tooth_thickness_for_bending_strength(
        self: Self, value: "_490.ToothThicknesses"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.ToothThicknesses"
        )
        self.wrapped.ChosenToothThicknessForBendingStrength = value

    @property
    def cylindrical_gear_profile_measurement(
        self: Self,
    ) -> "_1030.CylindricalGearProfileMeasurementType":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurementType"""
        temp = self.wrapped.CylindricalGearProfileMeasurement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1030",
            "CylindricalGearProfileMeasurementType",
        )(value)

    @cylindrical_gear_profile_measurement.setter
    @enforce_parameter_types
    def cylindrical_gear_profile_measurement(
        self: Self, value: "_1030.CylindricalGearProfileMeasurementType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )
        self.wrapped.CylindricalGearProfileMeasurement = value

    @property
    def dynamic_factor_method(self: Self) -> "_475.DynamicFactorMethods":
        """mastapy.gears.rating.cylindrical.DynamicFactorMethods"""
        temp = self.wrapped.DynamicFactorMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.DynamicFactorMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._475", "DynamicFactorMethods"
        )(value)

    @dynamic_factor_method.setter
    @enforce_parameter_types
    def dynamic_factor_method(self: Self, value: "_475.DynamicFactorMethods"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.DynamicFactorMethods"
        )
        self.wrapped.DynamicFactorMethod = value

    @property
    def enable_proportion_system_for_tip_alteration_coefficient(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EnableProportionSystemForTipAlterationCoefficient

        if temp is None:
            return False

        return temp

    @enable_proportion_system_for_tip_alteration_coefficient.setter
    @enforce_parameter_types
    def enable_proportion_system_for_tip_alteration_coefficient(
        self: Self, value: "bool"
    ):
        self.wrapped.EnableProportionSystemForTipAlterationCoefficient = (
            bool(value) if value is not None else False
        )

    @property
    def film_thickness_equation_for_scuffing(self: Self) -> "_486.ScuffingMethods":
        """mastapy.gears.rating.cylindrical.ScuffingMethods"""
        temp = self.wrapped.FilmThicknessEquationForScuffing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._486", "ScuffingMethods"
        )(value)

    @film_thickness_equation_for_scuffing.setter
    @enforce_parameter_types
    def film_thickness_equation_for_scuffing(self: Self, value: "_486.ScuffingMethods"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingMethods"
        )
        self.wrapped.FilmThicknessEquationForScuffing = value

    @property
    def gear_blank_factor_calculation_option(
        self: Self,
    ) -> "_476.GearBlankFactorCalculationOptions":
        """mastapy.gears.rating.cylindrical.GearBlankFactorCalculationOptions"""
        temp = self.wrapped.GearBlankFactorCalculationOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.GearBlankFactorCalculationOptions",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._476", "GearBlankFactorCalculationOptions"
        )(value)

    @gear_blank_factor_calculation_option.setter
    @enforce_parameter_types
    def gear_blank_factor_calculation_option(
        self: Self, value: "_476.GearBlankFactorCalculationOptions"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.GearBlankFactorCalculationOptions",
        )
        self.wrapped.GearBlankFactorCalculationOption = value

    @property
    def iso_tolerances_standard(
        self: Self,
    ) -> "overridable.Overridable_ISOToleranceStandard":
        """Overridable[mastapy.gears.ISOToleranceStandard]"""
        temp = self.wrapped.ISOTolerancesStandard

        if temp is None:
            return None

        value = overridable.Overridable_ISOToleranceStandard.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @iso_tolerances_standard.setter
    @enforce_parameter_types
    def iso_tolerances_standard(
        self: Self,
        value: "Union[_337.ISOToleranceStandard, Tuple[_337.ISOToleranceStandard, bool]]",
    ):
        wrapper_type = overridable.Overridable_ISOToleranceStandard.wrapper_type()
        enclosed_type = overridable.Overridable_ISOToleranceStandard.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.ISOTolerancesStandard = value

    @property
    def include_rim_thickness_factor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeRimThicknessFactor

        if temp is None:
            return False

        return temp

    @include_rim_thickness_factor.setter
    @enforce_parameter_types
    def include_rim_thickness_factor(self: Self, value: "bool"):
        self.wrapped.IncludeRimThicknessFactor = (
            bool(value) if value is not None else False
        )

    @property
    def internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.InternalGearRootFilletRadiusIsAlwaysEqualToBasicRackRootFilletRadius
        )

        if temp is None:
            return False

        return temp

    @internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius.setter
    @enforce_parameter_types
    def internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius(
        self: Self, value: "bool"
    ):
        self.wrapped.InternalGearRootFilletRadiusIsAlwaysEqualToBasicRackRootFilletRadius = (
            bool(value) if value is not None else False
        )

    @property
    def is_scuffing_licensed_for_current_rating_method(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsScuffingLicensedForCurrentRatingMethod

        if temp is None:
            return False

        return temp

    @property
    def limit_dynamic_factor_if_not_in_main_resonance_range_by_default(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.LimitDynamicFactorIfNotInMainResonanceRangeByDefault

        if temp is None:
            return False

        return temp

    @limit_dynamic_factor_if_not_in_main_resonance_range_by_default.setter
    @enforce_parameter_types
    def limit_dynamic_factor_if_not_in_main_resonance_range_by_default(
        self: Self, value: "bool"
    ):
        self.wrapped.LimitDynamicFactorIfNotInMainResonanceRangeByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def limit_micro_geometry_factor_for_the_dynamic_load_by_default(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.LimitMicroGeometryFactorForTheDynamicLoadByDefault

        if temp is None:
            return False

        return temp

    @limit_micro_geometry_factor_for_the_dynamic_load_by_default.setter
    @enforce_parameter_types
    def limit_micro_geometry_factor_for_the_dynamic_load_by_default(
        self: Self, value: "bool"
    ):
        self.wrapped.LimitMicroGeometryFactorForTheDynamicLoadByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def mean_coefficient_of_friction_flash_temperature_method(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @mean_coefficient_of_friction_flash_temperature_method.setter
    @enforce_parameter_types
    def mean_coefficient_of_friction_flash_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def micropitting_rating_method(self: Self) -> "_479.MicropittingRatingMethod":
        """mastapy.gears.rating.cylindrical.MicropittingRatingMethod"""
        temp = self.wrapped.MicropittingRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.MicropittingRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._479", "MicropittingRatingMethod"
        )(value)

    @micropitting_rating_method.setter
    @enforce_parameter_types
    def micropitting_rating_method(self: Self, value: "_479.MicropittingRatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.MicropittingRatingMethod"
        )
        self.wrapped.MicropittingRatingMethod = value

    @property
    def number_of_load_strips_for_basic_ltca(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLoadStripsForBasicLTCA

        if temp is None:
            return 0

        return temp

    @number_of_load_strips_for_basic_ltca.setter
    @enforce_parameter_types
    def number_of_load_strips_for_basic_ltca(self: Self, value: "int"):
        self.wrapped.NumberOfLoadStripsForBasicLTCA = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_along_profile_for_micropitting_calculation(
        self: Self,
    ) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsAlongProfileForMicropittingCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_micropitting_calculation.setter
    @enforce_parameter_types
    def number_of_points_along_profile_for_micropitting_calculation(
        self: Self, value: "int"
    ):
        self.wrapped.NumberOfPointsAlongProfileForMicropittingCalculation = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_along_profile_for_scuffing_calculation(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsAlongProfileForScuffingCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_scuffing_calculation.setter
    @enforce_parameter_types
    def number_of_points_along_profile_for_scuffing_calculation(
        self: Self, value: "int"
    ):
        self.wrapped.NumberOfPointsAlongProfileForScuffingCalculation = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_along_profile_for_tooth_flank_fracture_calculation(
        self: Self,
    ) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsAlongProfileForToothFlankFractureCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_tooth_flank_fracture_calculation.setter
    @enforce_parameter_types
    def number_of_points_along_profile_for_tooth_flank_fracture_calculation(
        self: Self, value: "int"
    ):
        self.wrapped.NumberOfPointsAlongProfileForToothFlankFractureCalculation = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_rotations_for_basic_ltca(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRotationsForBasicLTCA

        if temp is None:
            return 0

        return temp

    @number_of_rotations_for_basic_ltca.setter
    @enforce_parameter_types
    def number_of_rotations_for_basic_ltca(self: Self, value: "int"):
        self.wrapped.NumberOfRotationsForBasicLTCA = (
            int(value) if value is not None else 0
        )

    @property
    def permissible_bending_stress_method(self: Self) -> "_482.RatingMethod":
        """mastapy.gears.rating.cylindrical.RatingMethod"""
        temp = self.wrapped.PermissibleBendingStressMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.RatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._482", "RatingMethod"
        )(value)

    @permissible_bending_stress_method.setter
    @enforce_parameter_types
    def permissible_bending_stress_method(self: Self, value: "_482.RatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.RatingMethod"
        )
        self.wrapped.PermissibleBendingStressMethod = value

    @property
    def rating_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods":
        """EnumWithSelectedValue[mastapy.materials.CylindricalGearRatingMethods]"""
        temp = self.wrapped.RatingMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @rating_method.setter
    @enforce_parameter_types
    def rating_method(self: Self, value: "_254.CylindricalGearRatingMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RatingMethod = value

    @property
    def scuffing_rating_method_flash_temperature_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod":
        """EnumWithSelectedValue[mastapy.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod]"""
        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @scuffing_rating_method_flash_temperature_method.setter
    @enforce_parameter_types
    def scuffing_rating_method_flash_temperature_method(
        self: Self, value: "_484.ScuffingFlashTemperatureRatingMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ScuffingRatingMethodFlashTemperatureMethod = value

    @property
    def scuffing_rating_method_integral_temperature_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod":
        """EnumWithSelectedValue[mastapy.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod]"""
        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @scuffing_rating_method_integral_temperature_method.setter
    @enforce_parameter_types
    def scuffing_rating_method_integral_temperature_method(
        self: Self, value: "_485.ScuffingIntegralTemperatureRatingMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod = value

    @property
    def show_rating_settings_in_report(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowRatingSettingsInReport

        if temp is None:
            return False

        return temp

    @show_rating_settings_in_report.setter
    @enforce_parameter_types
    def show_rating_settings_in_report(self: Self, value: "bool"):
        self.wrapped.ShowRatingSettingsInReport = (
            bool(value) if value is not None else False
        )

    @property
    def show_vdi_rating_when_available(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowVDIRatingWhenAvailable

        if temp is None:
            return False

        return temp

    @show_vdi_rating_when_available.setter
    @enforce_parameter_types
    def show_vdi_rating_when_available(self: Self, value: "bool"):
        self.wrapped.ShowVDIRatingWhenAvailable = (
            bool(value) if value is not None else False
        )

    @property
    def tip_relief_in_scuffing_calculation(
        self: Self,
    ) -> "_489.TipReliefScuffingOptions":
        """mastapy.gears.rating.cylindrical.TipReliefScuffingOptions"""
        temp = self.wrapped.TipReliefInScuffingCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Cylindrical.TipReliefScuffingOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._489", "TipReliefScuffingOptions"
        )(value)

    @tip_relief_in_scuffing_calculation.setter
    @enforce_parameter_types
    def tip_relief_in_scuffing_calculation(
        self: Self, value: "_489.TipReliefScuffingOptions"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Cylindrical.TipReliefScuffingOptions"
        )
        self.wrapped.TipReliefInScuffingCalculation = value

    @property
    def tolerance_rounding_system(self: Self) -> "_1614.MeasurementSystem":
        """mastapy.utility.units_and_measurements.MeasurementSystem"""
        temp = self.wrapped.ToleranceRoundingSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.UnitsAndMeasurements.MeasurementSystem"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.units_and_measurements._1614", "MeasurementSystem"
        )(value)

    @tolerance_rounding_system.setter
    @enforce_parameter_types
    def tolerance_rounding_system(self: Self, value: "_1614.MeasurementSystem"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.UnitsAndMeasurements.MeasurementSystem"
        )
        self.wrapped.ToleranceRoundingSystem = value

    @property
    def use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.Use10ForContactRatioFactorContactForSpurGearsWithContactRatioLessThan20
        )

        if temp is None:
            return False

        return temp

    @use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20.setter
    @enforce_parameter_types
    def use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20(
        self: Self, value: "bool"
    ):
        self.wrapped.Use10ForContactRatioFactorContactForSpurGearsWithContactRatioLessThan20 = (
            bool(value) if value is not None else False
        )

    @property
    def use_diametral_pitch(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDiametralPitch

        if temp is None:
            return False

        return temp

    @use_diametral_pitch.setter
    @enforce_parameter_types
    def use_diametral_pitch(self: Self, value: "bool"):
        self.wrapped.UseDiametralPitch = bool(value) if value is not None else False

    @property
    def use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseInterpolatedSinglePairToothContactFactorForHCRHelicalGears
        )

        if temp is None:
            return False

        return temp

    @use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears.setter
    @enforce_parameter_types
    def use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears(
        self: Self, value: "bool"
    ):
        self.wrapped.UseInterpolatedSinglePairToothContactFactorForHCRHelicalGears = (
            bool(value) if value is not None else False
        )

    @property
    def use_ltca_stresses_in_gear_rating(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseLTCAStressesInGearRating

        if temp is None:
            return False

        return temp

    @use_ltca_stresses_in_gear_rating.setter
    @enforce_parameter_types
    def use_ltca_stresses_in_gear_rating(self: Self, value: "bool"):
        self.wrapped.UseLTCAStressesInGearRating = (
            bool(value) if value is not None else False
        )

    @property
    def use_point_of_highest_stress_to_calculate_face_load_factor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UsePointOfHighestStressToCalculateFaceLoadFactor

        if temp is None:
            return False

        return temp

    @use_point_of_highest_stress_to_calculate_face_load_factor.setter
    @enforce_parameter_types
    def use_point_of_highest_stress_to_calculate_face_load_factor(
        self: Self, value: "bool"
    ):
        self.wrapped.UsePointOfHighestStressToCalculateFaceLoadFactor = (
            bool(value) if value is not None else False
        )

    @property
    def vdi_rating_geometry_calculation_method(
        self: Self,
    ) -> "overridable.Overridable_CylindricalGearRatingMethods":
        """Overridable[mastapy.materials.CylindricalGearRatingMethods]"""
        temp = self.wrapped.VDIRatingGeometryCalculationMethod

        if temp is None:
            return None

        value = overridable.Overridable_CylindricalGearRatingMethods.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @vdi_rating_geometry_calculation_method.setter
    @enforce_parameter_types
    def vdi_rating_geometry_calculation_method(
        self: Self,
        value: "Union[_254.CylindricalGearRatingMethods, Tuple[_254.CylindricalGearRatingMethods, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_CylindricalGearRatingMethods.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_CylindricalGearRatingMethods.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.VDIRatingGeometryCalculationMethod = value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDesignAndRatingSettingsItem._Cast_CylindricalGearDesignAndRatingSettingsItem":
        return self._Cast_CylindricalGearDesignAndRatingSettingsItem(self)
