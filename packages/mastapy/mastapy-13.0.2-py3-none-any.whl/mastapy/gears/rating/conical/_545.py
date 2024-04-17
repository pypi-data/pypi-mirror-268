"""ConicalGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _947
    from mastapy.gears.rating.zerol_bevel import _374
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.gears.rating.straight_bevel_diff import _403
    from mastapy.gears.rating.spiral_bevel import _407
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_hypoid import _413
    from mastapy.gears.rating.klingelnberg_conical import _416
    from mastapy.gears.rating.hypoid import _443
    from mastapy.gears.rating.bevel import _559
    from mastapy.gears.rating.agma_gleason_conical import _570
    from mastapy.gears.rating import _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetRating",)


Self = TypeVar("Self", bound="ConicalGearSetRating")


class ConicalGearSetRating(_366.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetRating")

    class _Cast_ConicalGearSetRating:
        """Special nested class for casting ConicalGearSetRating to subclasses."""

        def __init__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
            parent: "ConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_366.GearSetRating":
            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_374.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _374

            return self._parent._cast(_374.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_400.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _400

            return self._parent._cast(_400.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_403.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _403

            return self._parent._cast(_403.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_407.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _407

            return self._parent._cast(_407.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _410

            return self._parent._cast(
                _410.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_416.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_443.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _443

            return self._parent._cast(_443.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_559.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _559

            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_570.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _570

            return self._parent._cast(_570.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "ConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self: Self) -> "_947.BevelHypoidGearRatingSettingsItem":
        """mastapy.gears.gear_designs.BevelHypoidGearRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearSetRating._Cast_ConicalGearSetRating":
        return self._Cast_ConicalGearSetRating(self)
