"""VDI2737InternalGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2737_INTERNAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.VDI", "VDI2737InternalGearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _522


__docformat__ = "restructuredtext en"
__all__ = ("VDI2737InternalGearSingleFlankRating",)


Self = TypeVar("Self", bound="VDI2737InternalGearSingleFlankRating")


class VDI2737InternalGearSingleFlankRating(_0.APIBase):
    """VDI2737InternalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _VDI2737_INTERNAL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VDI2737InternalGearSingleFlankRating")

    class _Cast_VDI2737InternalGearSingleFlankRating:
        """Special nested class for casting VDI2737InternalGearSingleFlankRating to subclasses."""

        def __init__(
            self: "VDI2737InternalGearSingleFlankRating._Cast_VDI2737InternalGearSingleFlankRating",
            parent: "VDI2737InternalGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def vdi2737_internal_gear_single_flank_rating(
            self: "VDI2737InternalGearSingleFlankRating._Cast_VDI2737InternalGearSingleFlankRating",
        ) -> "VDI2737InternalGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "VDI2737InternalGearSingleFlankRating._Cast_VDI2737InternalGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "VDI2737InternalGearSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def one_and_a_half_times_normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OneAndAHalfTimesNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def factor_of_loading_zone_of_tooth_contact_fatigue_fracture(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FactorOfLoadingZoneOfToothContactFatigueFracture

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_fracture_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueFractureSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_fracture_safety_factor_with_influence_of_rim(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueFractureSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_strength_with_influence_of_rim(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueStrengthWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor_for_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormFactorForCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def level_of_force_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LevelOfForceApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def local_stress_due_to_action_of_centrifugal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalStressDueToActionOfCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def local_stress_due_to_the_rim_bending_moment_outside_of_the_zone_of_tooth_contact(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LocalStressDueToTheRimBendingMomentOutsideOfTheZoneOfToothContact
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_stress_component_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanStressComponentCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_stress_component_2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanStressComponent2

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def nominal_stress_due_to_action_of_centrifugal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalStressDueToActionOfCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def notch_sensitivity_factor_for_fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchSensitivityFactorForFatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_planets(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @property
    def overlap_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverlapFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def peakto_peak_amplitude_of_local_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeaktoPeakAmplitudeOfLocalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def peakto_peak_amplitude_of_local_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeaktoPeakAmplitudeOfLocalStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def peakto_peak_amplitude_of_local_stress_stiff_rim(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeaktoPeakAmplitudeOfLocalStressStiffRim

        if temp is None:
            return 0.0

        return temp

    @property
    def position_of_maximum_local_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOfMaximumLocalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def position_of_maximum_local_stress_due_to_bending_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOfMaximumLocalStressDueToBendingMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def position_of_maximum_local_stress_due_to_tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOfMaximumLocalStressDueToTangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_in_transverse_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceInTransverseAction

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingName

        if temp is None:
            return ""

        return temp

    @property
    def reversed_fatigue_strength_of_tooth_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReversedFatigueStrengthOfToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_against_crack_initiation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyAgainstCrackInitiation

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_against_crack_initiation_with_influence_of_rim(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyAgainstCrackInitiationWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_against_permanent_deformation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorAgainstPermanentDeformation

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_against_permanent_deformation_with_influence_of_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorAgainstPermanentDeformationWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor_due_to_bending_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactorDueToBendingMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor_due_to_compression_by_radial_force(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactorDueToCompressionByRadialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor_due_to_tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactorDueToTangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor_due_to_tensile_stress_in_gear_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactorDueToTensileStressInGearRim

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_force_in_transverse_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceInTransverseAction

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_yield_strength_exceeded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TensileYieldStrengthExceeded

        if temp is None:
            return False

        return temp

    @property
    def tip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def iso_gear_rating(self: Self) -> "_522.ISO6336AbstractMetalGearSingleFlankRating":
        """mastapy.gears.rating.cylindrical.iso6336.ISO6336AbstractMetalGearSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOGearRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VDI2737InternalGearSingleFlankRating._Cast_VDI2737InternalGearSingleFlankRating":
        return self._Cast_VDI2737InternalGearSingleFlankRating(self)
