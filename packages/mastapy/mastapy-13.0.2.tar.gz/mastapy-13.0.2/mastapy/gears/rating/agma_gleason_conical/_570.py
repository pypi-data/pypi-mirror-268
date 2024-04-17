"""AGMAGleasonConicalGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _374
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.gears.rating.spiral_bevel import _407
    from mastapy.gears.rating.hypoid import _443
    from mastapy.gears.rating.bevel import _559
    from mastapy.gears.rating import _366, _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetRating")


class AGMAGleasonConicalGearSetRating(_545.ConicalGearSetRating):
    """AGMAGleasonConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetRating")

    class _Cast_AGMAGleasonConicalGearSetRating:
        """Special nested class for casting AGMAGleasonConicalGearSetRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            parent: "AGMAGleasonConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_545.ConicalGearSetRating":
            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_366.GearSetRating":
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_374.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _374

            return self._parent._cast(_374.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_400.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _400

            return self._parent._cast(_400.StraightBevelGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_407.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _407

            return self._parent._cast(_407.SpiralBevelGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_443.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _443

            return self._parent._cast(_443.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_559.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _559

            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "AGMAGleasonConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating":
        return self._Cast_AGMAGleasonConicalGearSetRating(self)
