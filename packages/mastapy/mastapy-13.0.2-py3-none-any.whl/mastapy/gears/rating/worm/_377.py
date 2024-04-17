"""WormGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.gear_designs.worm import _961
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("WormGearRating",)


Self = TypeVar("Self", bound="WormGearRating")


class WormGearRating(_364.GearRating):
    """WormGearRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearRating")

    class _Cast_WormGearRating:
        """Special nested class for casting WormGearRating to subclasses."""

        def __init__(
            self: "WormGearRating._Cast_WormGearRating", parent: "WormGearRating"
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "WormGearRating._Cast_WormGearRating",
        ) -> "_364.GearRating":
            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "WormGearRating._Cast_WormGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "WormGearRating._Cast_WormGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def worm_gear_rating(
            self: "WormGearRating._Cast_WormGearRating",
        ) -> "WormGearRating":
            return self._parent

        def __getattr__(self: "WormGearRating._Cast_WormGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearRating.TYPE"):
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
    def worm_gear(self: Self) -> "_961.WormGearDesign":
        """mastapy.gears.gear_designs.worm.WormGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearRating._Cast_WormGearRating":
        return self._Cast_WormGearRating(self)
