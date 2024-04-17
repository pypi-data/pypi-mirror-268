"""ConicalGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _432, _433, _434, _435, _436
    from mastapy.gears.rating.hypoid.standards import _445
    from mastapy.gears.rating.bevel.standards import _560, _562, _564


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSingleFlankRating",)


Self = TypeVar("Self", bound="ConicalGearSingleFlankRating")


class ConicalGearSingleFlankRating(_367.GearSingleFlankRating):
    """ConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSingleFlankRating")

    class _Cast_ConicalGearSingleFlankRating:
        """Special nested class for casting ConicalGearSingleFlankRating to subclasses."""

        def __init__(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
            parent: "ConicalGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_432.ISO10300SingleFlankRating":
            from mastapy.gears.rating.iso_10300 import _432

            return self._parent._cast(_432.ISO10300SingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_433.ISO10300SingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _433

            return self._parent._cast(_433.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_434.ISO10300SingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _434

            return self._parent._cast(_434.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_435.ISO10300SingleFlankRatingMethodB1":
            from mastapy.gears.rating.iso_10300 import _435

            return self._parent._cast(_435.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_436.ISO10300SingleFlankRatingMethodB2":
            from mastapy.gears.rating.iso_10300 import _436

            return self._parent._cast(_436.ISO10300SingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_445.GleasonHypoidGearSingleFlankRating":
            from mastapy.gears.rating.hypoid.standards import _445

            return self._parent._cast(_445.GleasonHypoidGearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_560.AGMASpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _560

            return self._parent._cast(_560.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_562.GleasonSpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _562

            return self._parent._cast(_562.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "_564.SpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _564

            return self._parent._cast(_564.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "ConicalGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating":
        return self._Cast_ConicalGearSingleFlankRating(self)
