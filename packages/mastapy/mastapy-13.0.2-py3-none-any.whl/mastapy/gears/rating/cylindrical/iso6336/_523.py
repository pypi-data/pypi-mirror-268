"""ISO6336AbstractMetalMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.cylindrical.iso6336 import _521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_METAL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ISO6336AbstractMetalMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _479, _484, _485, _462, _470
    from mastapy.gears.gear_designs.cylindrical import _1079
    from mastapy.gears.rating.cylindrical.iso6336 import _517, _522, _515, _519
    from mastapy.gears.rating.cylindrical.din3990 import _536
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336AbstractMetalMeshSingleFlankRating",)


Self = TypeVar("Self", bound="ISO6336AbstractMetalMeshSingleFlankRating")


class ISO6336AbstractMetalMeshSingleFlankRating(
    _521.ISO6336AbstractMeshSingleFlankRating
):
    """ISO6336AbstractMetalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_METAL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO6336AbstractMetalMeshSingleFlankRating"
    )

    class _Cast_ISO6336AbstractMetalMeshSingleFlankRating:
        """Special nested class for casting ISO6336AbstractMetalMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
            parent: "ISO6336AbstractMetalMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_515.ISO63361996MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _515

            return self._parent._cast(_515.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_517.ISO63362006MeshSingleFlankRating":
            return self._parent._cast(_517.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_519.ISO63362019MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _519

            return self._parent._cast(_519.ISO63362019MeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "_536.DIN3990MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _536

            return self._parent._cast(_536.DIN3990MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
        ) -> "ISO6336AbstractMetalMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating",
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
        self: Self, instance_to_wrap: "ISO6336AbstractMetalMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def approach_factor_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproachFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def approach_factor_of_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproachFactorOfMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def average_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_mean_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicMeanFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def bulk_temperature_for_micropitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BulkTemperatureForMicropitting

        if temp is None:
            return 0.0

        return temp

    @property
    def bulk_tooth_temperature_flash_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BulkToothTemperatureFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def bulk_tooth_temperature_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BulkToothTemperatureIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_exposure_time_flash_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactExposureTimeFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_exposure_time_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactExposureTimeIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_time_at_high_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactTimeAtHighVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_time_at_medium_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactTimeAtMediumVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def determinant_tangential_load_in_transverse_plane_for_transverse_load_factor(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DeterminantTangentialLoadInTransversePlaneForTransverseLoadFactor
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def drive_gear_tip_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DriveGearTipRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorSource

        if temp is None:
            return ""

        return temp

    @property
    def effective_equivalent_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveEquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_profile_form_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveProfileFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_tip_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveTipRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_transverse_base_pitch_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveTransverseBasePitchDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment_due_to_system_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignmentDueToSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_tip_relief_of_pinion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentTipReliefOfPinion

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_tip_relief_of_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentTipReliefOfWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_contact_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorContactSource

        if temp is None:
            return ""

        return temp

    @property
    def gear_blank_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBlankFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_at_pinion_tooth_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorAtPinionToothTip

        if temp is None:
            return 0.0

        return temp

    @property
    def helical_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelicalLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def highest_local_contact_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestLocalContactTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def initial_equivalent_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InitialEquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_contact_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralContactTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_path_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfPathOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def limiting_specific_lubricant_film_thickness_of_the_test_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingSpecificLubricantFilmThicknessOfTheTestGears

        if temp is None:
            return 0.0

        return temp

    @property
    def load_losses_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadLossesFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def local_hertzian_contact_stress_calculation_method(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalHertzianContactStressCalculationMethod

        if temp is None:
            return ""

        return temp

    @property
    def longest_contact_exposure_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LongestContactExposureTime

        if temp is None:
            return 0.0

        return temp

    @property
    def longest_contact_exposure_time_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LongestContactExposureTimeIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density_at_156_degrees_celsius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDensityAt156DegreesCelsius

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density_at_bulk_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDensityAtBulkToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density_at_micropitting_bulk_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDensityAtMicropittingBulkToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_dynamic_viscosity_at_tooth_temperature_micropitting(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDynamicViscosityAtToothTemperatureMicropitting

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_flash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorFlash

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_system_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationSystemFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def material_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def material_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_base_pitch_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBasePitchDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_profile_form_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumProfileFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCoefficientOfFrictionIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_calculated_constant_flash_temperature_method(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MeanCoefficientOfFrictionCalculatedConstantFlashTemperatureMethod
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_misalignment_due_to_manufacturing_deviations(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshMisalignmentDueToManufacturingDeviations

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def mesh_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def micro_geometry_factor_for_the_dynamic_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometryFactorForTheDynamicLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_rating_method(self: Self) -> "_479.MicropittingRatingMethod":
        """mastapy.gears.rating.cylindrical.MicropittingRatingMethod

        Note:
            This property is readonly.
        """
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

    @property
    def micropitting_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricant_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_specific_lubricant_film_thickness_in_the_contact_area(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSpecificLubricantFilmThicknessInTheContactArea

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_micro_geometry_lead_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDueToMicroGeometryLeadRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def multiple_path_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultiplePathFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_relative_radius_of_curvature_at_pitch_point_integral_temperature_method(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.NormalRelativeRadiusOfCurvatureAtPitchPointIntegralTemperatureMethod
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_unit_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalUnitLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def optimal_tip_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimalTipRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_specific_lubricant_film_thickness(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleSpecificLubricantFilmThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def permissible_specific_lubricant_film_thickness_from_figure_a1(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleSpecificLubricantFilmThicknessFromFigureA1

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_viscosity_coefficient_at_38_degrees_c(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureViscosityCoefficientAt38DegreesC

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_viscosity_coefficient_at_bulk_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureViscosityCoefficientAtBulkTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation_factor_for_the_dynamic_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviationFactorForTheDynamicLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mass_per_unit_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMassPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_welding_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeWeldingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def resonance_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResonanceRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def resonance_ratio_in_the_main_resonance_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResonanceRatioInTheMainResonanceRange

        if temp is None:
            return 0.0

        return temp

    @property
    def resonance_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResonanceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_micropitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorMicropitting

        if temp is None:
            return 0.0

        return temp

    @property
    def run_in_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunInFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def run_in_grade(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunInGrade

        if temp is None:
            return 0

        return temp

    @property
    def running_in(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunningIn

        if temp is None:
            return 0.0

        return temp

    @property
    def running_in_profile_form_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunningInProfileFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def running_in_allowance_equivalent_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunningInAllowanceEquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_load_safety_factor_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingLoadSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_rating_method_flash_temperature_method(
        self: Self,
    ) -> "_484.ScuffingFlashTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingFlashTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._484",
            "ScuffingFlashTemperatureRatingMethod",
        )(value)

    @property
    def scuffing_rating_method_integral_temperature_method(
        self: Self,
    ) -> "_485.ScuffingIntegralTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingIntegralTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._485",
            "ScuffingIntegralTemperatureRatingMethod",
        )(value)

    @property
    def scuffing_safety_factor_flash_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature_at_high_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureAtHighVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature_at_medium_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureAtMediumVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature_gradient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureGradient

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature_gradient_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureGradientIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_temperature_method(
        self: Self,
    ) -> "_1079.ScuffingTemperatureMethodsISO":
        """mastapy.gears.gear_designs.cylindrical.ScuffingTemperatureMethodsISO

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsISO",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1079",
            "ScuffingTemperatureMethodsISO",
        )(value)

    @property
    def single_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_material_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMaterialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def test_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TestTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_single_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalSingleStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def thermo_elastic_factor_of_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermoElasticFactorOfMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_calculated(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefCalculated

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_factor_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_factor_for_micropitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefFactorForMicropitting

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_stiffness_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothStiffnessCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_base_pitch_deviation_factor_for_the_dynamic_load(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseBasePitchDeviationFactorForTheDynamicLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_unit_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseUnitLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def user_input_scuffing_integral_temperature_for_long_contact_times(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserInputScuffingIntegralTemperatureForLongContactTimes

        if temp is None:
            return 0.0

        return temp

    @property
    def user_input_scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserInputScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def user_input_scuffing_temperature_for_long_contact_times(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserInputScuffingTemperatureForLongContactTimes

        if temp is None:
            return 0.0

        return temp

    @property
    def single_flank_rating_of_test_gears_for_micropitting(
        self: Self,
    ) -> "_517.ISO63362006MeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.iso6336.ISO63362006MeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleFlankRatingOfTestGearsForMicropitting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sorted_micro_pitting_results(
        self: Self,
    ) -> "_462.CylindricalGearMicroPittingResults":
        """mastapy.gears.rating.cylindrical.CylindricalGearMicroPittingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SortedMicroPittingResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isodin_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_522.ISO6336AbstractMetalGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ISO6336AbstractMetalGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISODINCylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336AbstractMetalMeshSingleFlankRating._Cast_ISO6336AbstractMetalMeshSingleFlankRating":
        return self._Cast_ISO6336AbstractMetalMeshSingleFlankRating(self)
