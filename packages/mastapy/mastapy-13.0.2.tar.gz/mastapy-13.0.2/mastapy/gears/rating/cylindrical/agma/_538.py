"""AGMA2101MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2101_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA", "AGMA2101MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.materials import _258
    from mastapy.gears.gear_designs.cylindrical import _1031, _1078
    from mastapy.gears.rating.cylindrical.agma import _540, _537
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("AGMA2101MeshSingleFlankRating",)


Self = TypeVar("Self", bound="AGMA2101MeshSingleFlankRating")


class AGMA2101MeshSingleFlankRating(_470.CylindricalMeshSingleFlankRating):
    """AGMA2101MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA2101_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA2101MeshSingleFlankRating")

    class _Cast_AGMA2101MeshSingleFlankRating:
        """Special nested class for casting AGMA2101MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating",
            parent: "AGMA2101MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(
            self: "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating",
        ) -> "AGMA2101MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA2101MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_length_of_line_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveLengthOfLineOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def actual_tangential_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualTangentialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_standard_deviation_of_scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximateStandardDeviationOfScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def average_roughness_ra(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageRoughnessRa

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_span(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSpan

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_derating_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedDeratingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def composite_surface_roughness_at_fc(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompositeSurfaceRoughnessAtFC

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicViscosityAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def elastic_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def entraining_velocity_at_end_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntrainingVelocityAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def entraining_velocity_at_pitch_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntrainingVelocityAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def entraining_velocity_at_start_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntrainingVelocityAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def fifth_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FifthDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def filter_cutoff_wavelength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilterCutoffWavelength

        if temp is None:
            return 0.0

        return temp

    @property
    def first_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def fourth_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FourthDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def gearing_type(self: Self) -> "_258.GearingTypes":
        """mastapy.materials.GearingTypes

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Materials.GearingTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.materials._258", "GearingTypes")(
            value
        )

    @property
    def geometry_factor_i(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorI

        if temp is None:
            return 0.0

        return temp

    @property
    def helical_overlap_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelicalOverlapFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def improved_gearing(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImprovedGearing

        if temp is None:
            return False

        return temp

    @property
    def lead_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorSource

        if temp is None:
            return ""

        return temp

    @property
    def load_sharing_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def materials_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsParameter

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
    def mean_minimum_specific_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanMinimumSpecificFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_alignment_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignmentCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_alignment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_alignment_factor_empirical_constant_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignmentFactorEmpiricalConstantA

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_alignment_factor_empirical_constant_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignmentFactorEmpiricalConstantB

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_alignment_factor_empirical_constant_c(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignmentFactorEmpiricalConstantC

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_contact_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumContactLength

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_film_thickness_isothermal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFilmThicknessIsothermal

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_film_thickness_with_inlet_shear_heating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFilmThicknessWithInletShearHeating

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_length_of_contact_lines_per_unit_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLengthOfContactLinesPerUnitModule

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_specific_film_thickness_isothermal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSpecificFilmThicknessIsothermal

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_specific_film_thickness_with_inlet_shear_heating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSpecificFilmThicknessWithInletShearHeating

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_operating_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalOperatingLoad

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
    def operating_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def parameter_for_calculating_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterForCalculatingToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_offset_from_bearing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionOffsetFromBearing

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_proportion_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionProportionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_proportion_modifier(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionProportionModifier

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_viscosity_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureViscosityCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def probability_of_scuffing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProbabilityOfScuffing

        if temp is None:
            return 0.0

        return temp

    @property
    def probability_of_wear_isothermal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProbabilityOfWearIsothermal

        if temp is None:
            return 0.0

        return temp

    @property
    def probability_of_wear_with_inlet_shear_heating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProbabilityOfWearWithInletShearHeating

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_modification(self: Self) -> "_1031.CylindricalGearProfileModifications":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileModifications

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileModification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileModifications",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1031",
            "CylindricalGearProfileModifications",
        )(value)

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceTemperature

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
    def scuffing_temperature_method(
        self: Self,
    ) -> "_1078.ScuffingTemperatureMethodsAGMA":
        """mastapy.gears.gear_designs.cylindrical.ScuffingTemperatureMethodsAGMA

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsAGMA",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1078",
            "ScuffingTemperatureMethodsAGMA",
        )(value)

    @property
    def second_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def sixth_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SixthDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_end_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_pitch_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_start_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def standard_deviation_of_the_minimum_specific_film_thickness(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StandardDeviationOfTheMinimumSpecificFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def sump_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumpTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_condition_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_roughness_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughnessConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_viscosity_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureViscosityCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def third_distance_along_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThirdDistanceAlongLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def transmission_accuracy_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionAccuracyNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_metric_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseMetricModule

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_reduction_factor_factors_and_exponents(
        self: Self,
    ) -> "_540.ThermalReductionFactorFactorsAndExponents":
        """mastapy.gears.rating.cylindrical.agma.ThermalReductionFactorFactorsAndExponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalReductionFactorFactorsAndExponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_537.AGMA2101GearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.agma.AGMA2101GearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_537.AGMA2101GearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.agma.AGMA2101GearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMACylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMA2101MeshSingleFlankRating._Cast_AGMA2101MeshSingleFlankRating":
        return self._Cast_AGMA2101MeshSingleFlankRating(self)
