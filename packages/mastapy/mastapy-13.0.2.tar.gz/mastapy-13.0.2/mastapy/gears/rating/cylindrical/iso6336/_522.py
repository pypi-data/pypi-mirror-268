"""ISO6336AbstractMetalGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.cylindrical.iso6336 import _520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ISO6336AbstractMetalGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _514, _516, _518
    from mastapy.gears.rating.cylindrical.din3990 import _535
    from mastapy.gears.rating.cylindrical import _468
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336AbstractMetalGearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO6336AbstractMetalGearSingleFlankRating")


class ISO6336AbstractMetalGearSingleFlankRating(
    _520.ISO6336AbstractGearSingleFlankRating
):
    """ISO6336AbstractMetalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO6336AbstractMetalGearSingleFlankRating"
    )

    class _Cast_ISO6336AbstractMetalGearSingleFlankRating:
        """Special nested class for casting ISO6336AbstractMetalGearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
            parent: "ISO6336AbstractMetalGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_520.ISO6336AbstractGearSingleFlankRating":
            return self._parent._cast(_520.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso63361996_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_514.ISO63361996GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _514

            return self._parent._cast(_514.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_516.ISO63362006GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _516

            return self._parent._cast(_516.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_518.ISO63362019GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO63362019GearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "_535.DIN3990GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _535

            return self._parent._cast(_535.DIN3990GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
        ) -> "ISO6336AbstractMetalGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "ISO6336AbstractMetalGearSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_deviation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def life_factor_for_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForStaticBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForStaticContactStress

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
    def lubricant_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_of_inertia_per_unit_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentOfInertiaPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def relative_individual_gear_mass_per_unit_face_width_referenced_to_line_of_action(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def shot_peening_bending_stress_benefit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShotPeeningBendingStressBenefit

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pair_tooth_contact_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePairToothContactFactor

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
    def size_factor_tooth_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def static_size_factor_tooth_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkHardeningFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating":
        return self._Cast_ISO6336AbstractMetalGearSingleFlankRating(self)
