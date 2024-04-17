"""KlingelnbergCycloPalloidConicalGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _420


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSingleFlankRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSingleFlankRating")


class KlingelnbergCycloPalloidConicalGearSingleFlankRating(_367.GearSingleFlankRating):
    """KlingelnbergCycloPalloidConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSingleFlankRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
            parent: "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
        ) -> "_420.KlingelnbergCycloPalloidHypoidGearSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _420

            return self._parent._cast(
                _420.KlingelnbergCycloPalloidHypoidGearSingleFlankRating
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
        ) -> "KlingelnbergCycloPalloidConicalGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStressNumber

        if temp is None:
            return 0.0

        return temp

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
    def bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankRoughness

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
    def rated_tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedTangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_sensitivity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSensitivityFactor

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
    def tangential_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialSpeed

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating(self)
