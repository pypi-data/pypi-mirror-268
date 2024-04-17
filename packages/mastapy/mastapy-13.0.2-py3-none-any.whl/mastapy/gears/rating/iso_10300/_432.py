"""ISO10300SingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.conical import _546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300SingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _392
    from mastapy.gears.rating.iso_10300 import _433, _434, _435, _436
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300SingleFlankRating",)


Self = TypeVar("Self", bound="ISO10300SingleFlankRating")
T = TypeVar("T", bound="_392.VirtualCylindricalGearBasic")


class ISO10300SingleFlankRating(_546.ConicalGearSingleFlankRating, Generic[T]):
    """ISO10300SingleFlankRating

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO10300SingleFlankRating")

    class _Cast_ISO10300SingleFlankRating:
        """Special nested class for casting ISO10300SingleFlankRating to subclasses."""

        def __init__(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
            parent: "ISO10300SingleFlankRating",
        ):
            self._parent = parent

        @property
        def conical_gear_single_flank_rating(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_546.ConicalGearSingleFlankRating":
            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_433.ISO10300SingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _433

            return self._parent._cast(_433.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_434.ISO10300SingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _434

            return self._parent._cast(_434.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_435.ISO10300SingleFlankRatingMethodB1":
            from mastapy.gears.rating.iso_10300 import _435

            return self._parent._cast(_435.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "_436.ISO10300SingleFlankRatingMethodB2":
            from mastapy.gears.rating.iso_10300 import _436

            return self._parent._cast(_436.ISO10300SingleFlankRatingMethodB2)

        @property
        def iso10300_single_flank_rating(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating",
        ) -> "ISO10300SingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO10300SingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_stress_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_number_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def constant_lubricant_film_factor_czl_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstantLubricantFilmFactorCZLMethodB

        if temp is None:
            return 0.0

        return temp

    @property
    def constant_roughness_factor_czr_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstantRoughnessFactorCZRMethodB

        if temp is None:
            return 0.0

        return temp

    @property
    def constant_speed_factor_czv_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstantSpeedFactorCZVMethodB

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
    def life_factor_for_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorMethodB

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalPower

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tangential_force_of_bevel_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTangentialForceOfBevelGears

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tangential_speed_at_mean_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTangentialSpeedAtMeanPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def product_of_lubricant_film_influence_factors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProductOfLubricantFilmInfluenceFactors

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mass_per_unit_face_width_reference_to_line_of_action(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMassPerUnitFaceWidthReferenceToLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_contact_stress_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorForContactStressMethodB

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pitch_deviation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePitchDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

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
    def size_factor_for_case_flame_induction_hardened_steels_nitrided_or_nitro_carburized_steels(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.SizeFactorForCaseFlameInductionHardenedSteelsNitridedOrNitroCarburizedSteels
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_grey_cast_iron_and_spheroidal_cast_iron(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForGreyCastIronAndSpheroidalCastIron

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_structural_and_through_hardened_steels_spheroidal_cast_iron_perlitic_malleable_cast_iron(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.SizeFactorForStructuralAndThroughHardenedSteelsSpheroidalCastIronPerliticMalleableCastIron
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_factor_method_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactorMethodB

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
    ) -> "ISO10300SingleFlankRating._Cast_ISO10300SingleFlankRating":
        return self._Cast_ISO10300SingleFlankRating(self)
