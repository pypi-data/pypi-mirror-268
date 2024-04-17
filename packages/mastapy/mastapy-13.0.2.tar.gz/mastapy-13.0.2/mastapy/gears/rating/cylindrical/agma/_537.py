"""AGMA2101GearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.cylindrical import _468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2101_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA", "AGMA2101GearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("AGMA2101GearSingleFlankRating",)


Self = TypeVar("Self", bound="AGMA2101GearSingleFlankRating")


class AGMA2101GearSingleFlankRating(_468.CylindricalGearSingleFlankRating):
    """AGMA2101GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA2101_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA2101GearSingleFlankRating")

    class _Cast_AGMA2101GearSingleFlankRating:
        """Special nested class for casting AGMA2101GearSingleFlankRating to subclasses."""

        def __init__(
            self: "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating",
            parent: "AGMA2101GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_single_flank_rating(
            self: "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def agma2101_gear_single_flank_rating(
            self: "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating",
        ) -> "AGMA2101GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA2101GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_bending_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTransmittedPowerForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_bending_strength_at_unity_service_factor(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AllowableTransmittedPowerForBendingStrengthAtUnityServiceFactor
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_pitting_resistance_at_unity_service_factor(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AllowableTransmittedPowerForPittingResistanceAtUnityServiceFactor
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_unit_load_for_bending_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableUnitLoadForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def backup_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackupRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_lewis_parabola(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfLewisParabola

        if temp is None:
            return 0.0

        return temp

    @property
    def helical_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelicalFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tolerance_diameter_for_the_agma_standard(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumToleranceDiameterForTheAGMAStandard

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tolerance_diameter_for_the_agma_standard(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumToleranceDiameterForTheAGMAStandard

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_resistance_power_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingResistancePowerRating

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pitch_deviation_agma(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePitchDeviationAGMA

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def stress_correction_factor_agma(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactorAGMA

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_for_pitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCycleFactorForPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToleranceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_at_critical_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessAtCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def unit_load_for_bending_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnitLoadForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating":
        return self._Cast_AGMA2101GearSingleFlankRating(self)
