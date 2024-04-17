"""GearFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FLANK_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearFlankRating")

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _459, _460


__docformat__ = "restructuredtext en"
__all__ = ("GearFlankRating",)


Self = TypeVar("Self", bound="GearFlankRating")


class GearFlankRating(_0.APIBase):
    """GearFlankRating

    This is a mastapy class.
    """

    TYPE = _GEAR_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearFlankRating")

    class _Cast_GearFlankRating:
        """Special nested class for casting GearFlankRating to subclasses."""

        def __init__(
            self: "GearFlankRating._Cast_GearFlankRating", parent: "GearFlankRating"
        ):
            self._parent = parent

        @property
        def cylindrical_gear_flank_duty_cycle_rating(
            self: "GearFlankRating._Cast_GearFlankRating",
        ) -> "_459.CylindricalGearFlankDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _459

            return self._parent._cast(_459.CylindricalGearFlankDutyCycleRating)

        @property
        def cylindrical_gear_flank_rating(
            self: "GearFlankRating._Cast_GearFlankRating",
        ) -> "_460.CylindricalGearFlankRating":
            from mastapy.gears.rating.cylindrical import _460

            return self._parent._cast(_460.CylindricalGearFlankRating)

        @property
        def gear_flank_rating(
            self: "GearFlankRating._Cast_GearFlankRating",
        ) -> "GearFlankRating":
            return self._parent

        def __getattr__(self: "GearFlankRating._Cast_GearFlankRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cycles

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "GearFlankRating._Cast_GearFlankRating":
        return self._Cast_GearFlankRating(self)
