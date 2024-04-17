"""WormGearSetDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetDutyCycleRating",)


Self = TypeVar("Self", bound="WormGearSetDutyCycleRating")


class WormGearSetDutyCycleRating(_365.GearSetDutyCycleRating):
    """WormGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetDutyCycleRating")

    class _Cast_WormGearSetDutyCycleRating:
        """Special nested class for casting WormGearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
            parent: "WormGearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
        ) -> "_365.GearSetDutyCycleRating":
            return self._parent._cast(_365.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
        ) -> "WormGearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating":
        return self._Cast_WormGearSetDutyCycleRating(self)
