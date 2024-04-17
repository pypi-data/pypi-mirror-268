"""CylindricalMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalMeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1077, _1076
    from mastapy.gears import _324
    from mastapy.materials import _270
    from mastapy.gears.rating.cylindrical import _457, _465, _468
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493, _495, _497
    from mastapy.gears.rating.cylindrical.iso6336 import _515, _517, _519, _521, _523
    from mastapy.gears.rating.cylindrical.din3990 import _536
    from mastapy.gears.rating.cylindrical.agma import _538


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshSingleFlankRating",)


Self = TypeVar("Self", bound="CylindricalMeshSingleFlankRating")


class CylindricalMeshSingleFlankRating(_369.MeshSingleFlankRating):
    """CylindricalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshSingleFlankRating")

    class _Cast_CylindricalMeshSingleFlankRating:
        """Special nested class for casting CylindricalMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
            parent: "CylindricalMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493

            return self._parent._cast(
                _493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
            )

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_495.PlasticGearVDI2736AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495

            return self._parent._cast(
                _495.PlasticGearVDI2736AbstractMeshSingleFlankRating
            )

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_497.PlasticPlasticVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497

            return self._parent._cast(_497.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_515.ISO63361996MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _515

            return self._parent._cast(_515.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_517.ISO63362006MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _517

            return self._parent._cast(_517.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_519.ISO63362019MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _519

            return self._parent._cast(_519.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _521

            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_523.ISO6336AbstractMetalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_536.DIN3990MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _536

            return self._parent._cast(_536.DIN3990MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "_538.AGMA2101MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.agma import _538

            return self._parent._cast(_538.AGMA2101MeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
        ) -> "CylindricalMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalMeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_length_of_the_line_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveLengthOfTheLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_method_flash_temperature_method(
        self: Self,
    ) -> "_1077.ScuffingCoefficientOfFrictionMethods":
        """mastapy.gears.gear_designs.cylindrical.ScuffingCoefficientOfFrictionMethods

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingCoefficientOfFrictionMethods",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1077",
            "ScuffingCoefficientOfFrictionMethods",
        )(value)

    @property
    def contact_ratio_source(self: Self) -> "_324.ContactRatioDataSource":
        """mastapy.gears.ContactRatioDataSource

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.ContactRatioDataSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._324", "ContactRatioDataSource"
        )(value)

    @property
    def duration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_arithmetic_mean_roughness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveArithmeticMeanRoughness

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def elasticity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorContact

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
    def gear_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def line_of_action_parameter_of_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineOfActionParameterOfMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return ""

        return temp

    @property
    def load_sharing_factor_of_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorOfMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_dynamic_viscosity_at_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDynamicViscosityAtToothTemperature

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
    def mean_coefficient_of_friction_of_maximum_flash_temperature(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCoefficientOfFrictionOfMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_dynamic_factor_for_wind_turbine_applications(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumDynamicFactorForWindTurbineApplications

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_face_load_factor_for_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFaceLoadFactorForContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentSource

        if temp is None:
            return ""

        return temp

    @property
    def nominal_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_radial_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalRadialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tangential_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTangentialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_transverse_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTransverseLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_roll_angle_at_highest_point_of_single_tooth_contact(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRollAngleAtHighestPointOfSingleToothContact

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_at_operating_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityAtOperatingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_separating_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialSeparatingLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def reduced_modulus_of_elasticity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReducedModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_angle_of_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollAngleOfMaximumFlashTemperature

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
    def signed_gear_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedGearRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def slideto_roll_ratio_at_end_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidetoRollRatioAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def slideto_roll_ratio_at_pitch_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidetoRollRatioAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def slideto_roll_ratio_at_start_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidetoRollRatioAtStartOfActiveProfile

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
    def tangential_velocity_at_reference_cylinder(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialVelocityAtReferenceCylinder

        if temp is None:
            return 0.0

        return temp

    @property
    def transmitted_tangential_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmittedTangentialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatio

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
    def user_specified_coefficient_of_friction_flash_temperature_method(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedCoefficientOfFrictionFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def welding_structural_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WeldingStructuralFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_detail(self: Self) -> "_270.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_settings(
        self: Self,
    ) -> "_457.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing(self: Self) -> "_1076.Scuffing":
        """mastapy.gears.gear_designs.cylindrical.Scuffing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Scuffing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sorted_scuffing_results(self: Self) -> "_465.CylindricalGearScuffingResults":
        """mastapy.gears.rating.cylindrical.CylindricalGearScuffingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SortedScuffingResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sorted_scuffing_results_without_special_values(
        self: Self,
    ) -> "_465.CylindricalGearScuffingResults":
        """mastapy.gears.rating.cylindrical.CylindricalGearScuffingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SortedScuffingResultsWithoutSpecialValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_468.CylindricalGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearSingleFlankRating]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshSingleFlankRating._Cast_CylindricalMeshSingleFlankRating":
        return self._Cast_CylindricalMeshSingleFlankRating(self)
