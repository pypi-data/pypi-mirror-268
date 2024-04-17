"""WormGearDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.rating.worm import _378, _377
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("WormGearDutyCycleRating",)


Self = TypeVar("Self", bound="WormGearDutyCycleRating")


class WormGearDutyCycleRating(_361.GearDutyCycleRating):
    """WormGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearDutyCycleRating")

    class _Cast_WormGearDutyCycleRating:
        """Special nested class for casting WormGearDutyCycleRating to subclasses."""

        def __init__(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating",
            parent: "WormGearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating",
        ) -> "_361.GearDutyCycleRating":
            return self._parent._cast(_361.GearDutyCycleRating)

        @property
        def abstract_gear_rating(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def worm_gear_duty_cycle_rating(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating",
        ) -> "WormGearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_design_duty_cycle(self: Self) -> "_378.WormGearSetDutyCycleRating":
        """mastapy.gears.rating.worm.WormGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_set_design_duty_cycle(
        self: Self,
    ) -> "_378.WormGearSetDutyCycleRating":
        """mastapy.gears.rating.worm.WormGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_377.WormGearRating]":
        """List[mastapy.gears.rating.worm.WormGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_ratings(self: Self) -> "List[_377.WormGearRating]":
        """List[mastapy.gears.rating.worm.WormGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormGearDutyCycleRating._Cast_WormGearDutyCycleRating":
        return self._Cast_WormGearDutyCycleRating(self)
