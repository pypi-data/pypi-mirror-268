"""CylindricalGearFlankDutyCycleRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearFlankDutyCycleRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFlankDutyCycleRating",)


Self = TypeVar("Self", bound="CylindricalGearFlankDutyCycleRating")


class CylindricalGearFlankDutyCycleRating(_362.GearFlankRating):
    """CylindricalGearFlankDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFlankDutyCycleRating")

    class _Cast_CylindricalGearFlankDutyCycleRating:
        """Special nested class for casting CylindricalGearFlankDutyCycleRating to subclasses."""

        def __init__(
            self: "CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating",
            parent: "CylindricalGearFlankDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_flank_rating(
            self: "CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating",
        ) -> "_362.GearFlankRating":
            return self._parent._cast(_362.GearFlankRating)

        @property
        def cylindrical_gear_flank_duty_cycle_rating(
            self: "CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating",
        ) -> "CylindricalGearFlankDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating",
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
        self: Self, instance_to_wrap: "CylindricalGearFlankDutyCycleRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating"
    ):
        return self._Cast_CylindricalGearFlankDutyCycleRating(self)
