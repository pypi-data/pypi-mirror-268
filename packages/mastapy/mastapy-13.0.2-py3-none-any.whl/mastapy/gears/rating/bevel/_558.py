"""BevelGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.agma_gleason_conical import _569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel", "BevelGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _373
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.gears.rating.spiral_bevel import _406
    from mastapy.gears.rating.conical import _543
    from mastapy.gears.rating import _364, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearRating",)


Self = TypeVar("Self", bound="BevelGearRating")


class BevelGearRating(_569.AGMAGleasonConicalGearRating):
    """BevelGearRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearRating")

    class _Cast_BevelGearRating:
        """Special nested class for casting BevelGearRating to subclasses."""

        def __init__(
            self: "BevelGearRating._Cast_BevelGearRating", parent: "BevelGearRating"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_569.AGMAGleasonConicalGearRating":
            return self._parent._cast(_569.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_543.ConicalGearRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearRating)

        @property
        def gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_373.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _373

            return self._parent._cast(_373.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_399.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _399

            return self._parent._cast(_399.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_406.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _406

            return self._parent._cast(_406.SpiralBevelGearRating)

        @property
        def bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "BevelGearRating":
            return self._parent

        def __getattr__(self: "BevelGearRating._Cast_BevelGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearRating._Cast_BevelGearRating":
        return self._Cast_BevelGearRating(self)
