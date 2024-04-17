"""ISO10300SingleFlankRatingMethodB1"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING_METHOD_B1 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300SingleFlankRatingMethodB1"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300SingleFlankRatingMethodB1",)


Self = TypeVar("Self", bound="ISO10300SingleFlankRatingMethodB1")


class ISO10300SingleFlankRatingMethodB1(
    _432.ISO10300SingleFlankRating["_393.VirtualCylindricalGearISO10300MethodB1"]
):
    """ISO10300SingleFlankRatingMethodB1

    This is a mastapy class.
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING_METHOD_B1
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO10300SingleFlankRatingMethodB1")

    class _Cast_ISO10300SingleFlankRatingMethodB1:
        """Special nested class for casting ISO10300SingleFlankRatingMethodB1 to subclasses."""

        def __init__(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
            parent: "ISO10300SingleFlankRatingMethodB1",
        ):
            self._parent = parent

        @property
        def iso10300_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
        ) -> "_432.ISO10300SingleFlankRating":
            return self._parent._cast(_432.ISO10300SingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
        ) -> "_546.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating_method_b1(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
        ) -> "ISO10300SingleFlankRatingMethodB1":
            return self._parent

        def __getattr__(
            self: "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1",
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
        self: Self, instance_to_wrap: "ISO10300SingleFlankRatingMethodB1.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auxiliary_angle_for_tooth_form_and_tooth_correction_factor(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryAngleForToothFormAndToothCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_e_for_generated_gear_coast_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesEForGeneratedGearCoastFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_e_for_generated_gear_drive_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesEForGeneratedGearDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_e_for_non_generated_gear_coast_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesEForNonGeneratedGearCoastFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_e_for_non_generated_gear_drive_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesEForNonGeneratedGearDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_g_for_coast_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesGForCoastSide

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_g_for_drive_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesGForDriveSide

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_h_for_coast_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesHForCoastSide

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_h_for_drive_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesHForDriveSide

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_theta_for_coast_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesThetaForCoastSide

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_quantities_theta_for_drive_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryQuantitiesThetaForDriveSide

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_moment_arm_for_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArmForGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_moment_arm_for_non_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArmForNonGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def la(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.La

        if temp is None:
            return 0.0

        return temp

    @property
    def load_application_angle_at_tooth_tip_of_virtual_cylindrical_gear_method_b1(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadApplicationAngleAtToothTipOfVirtualCylindricalGearMethodB1
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_value_of_root_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalValueOfRootStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_tooth_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtToothTip

        if temp is None:
            return 0.0

        return temp

    @property
    def notch_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_use_bevel_slip_factor_method_b1(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStressUseBevelSlipFactorMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactorForMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_stress_drop_in_notch_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeStressDropInNotchRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_grey_cast_iron_nitrided_and_nitro_carburized_steels_1_mum_mean_roughness_40_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForGreyCastIronNitridedAndNitroCarburizedSteels1MumMeanRoughness40Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_grey_cast_iron_nitrided_and_nitro_carburized_steels_mean_roughness_1_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForGreyCastIronNitridedAndNitroCarburizedSteelsMeanRoughness1Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_non_hardened_steels_1_mum_mean_roughness_40_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForNonHardenedSteels1MumMeanRoughness40Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_non_hardened_steels_mean_roughness_1_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForNonHardenedSteelsMeanRoughness1Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_through_hardened_and_case_hardened_steels_1_mum_mean_roughness_40_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForThroughHardenedAndCaseHardenedSteels1MumMeanRoughness40Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_through_hardened_and_case_hardened_steels_mean_roughness_1_mum(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeSurfaceConditionFactorForThroughHardenedAndCaseHardenedSteelsMeanRoughness1Mum
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceConditionFactorForMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_generated_gear_coast_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForGeneratedGearCoastFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_generated_gear_drive_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForGeneratedGearDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_non_generated_gear_coast_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForNonGeneratedGearCoastFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_for_non_generated_gear_drive_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusForNonGeneratedGearDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_bending_for_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorBendingForMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_contact_for_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorContactForMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_contact_use_bevel_slip_factor_for_method_b1(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorContactUseBevelSlipFactorForMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor_for_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactorForGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor_for_non_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactorForNonGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_for_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordalThicknessForGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_for_non_generated_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordalThicknessForNonGeneratedGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_per_flank_for_generated_gear_coast_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordalThicknessPerFlankForGeneratedGearCoastFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_per_flank_for_generated_gear_drive_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordalThicknessPerFlankForGeneratedGearDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_per_flank_for_non_generated_gear_coast_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ToothRootChordalThicknessPerFlankForNonGeneratedGearCoastFlank
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chordal_thickness_per_flank_for_non_generated_gear_drive_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ToothRootChordalThicknessPerFlankForNonGeneratedGearDriveFlank
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300SingleFlankRatingMethodB1._Cast_ISO10300SingleFlankRatingMethodB1":
        return self._Cast_ISO10300SingleFlankRatingMethodB1(self)
