"""ConicalGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.rating.zerol_bevel import _373
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.gears.rating.straight_bevel_diff import _402
    from mastapy.gears.rating.spiral_bevel import _406
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_hypoid import _412
    from mastapy.gears.rating.klingelnberg_conical import _415
    from mastapy.gears.rating.hypoid import _442
    from mastapy.gears.rating.bevel import _558
    from mastapy.gears.rating.agma_gleason_conical import _569
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearRating",)


Self = TypeVar("Self", bound="ConicalGearRating")


class ConicalGearRating(_364.GearRating):
    """ConicalGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearRating")

    class _Cast_ConicalGearRating:
        """Special nested class for casting ConicalGearRating to subclasses."""

        def __init__(
            self: "ConicalGearRating._Cast_ConicalGearRating",
            parent: "ConicalGearRating",
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_364.GearRating":
            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_373.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _373

            return self._parent._cast(_373.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_399.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _399

            return self._parent._cast(_399.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_402.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _402

            return self._parent._cast(_402.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_406.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _406

            return self._parent._cast(_406.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_409.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_412.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_415.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _415

            return self._parent._cast(_415.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_442.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _442

            return self._parent._cast(_442.HypoidGearRating)

        @property
        def bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_558.BevelGearRating":
            from mastapy.gears.rating.bevel import _558

            return self._parent._cast(_558.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_569.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _569

            return self._parent._cast(_569.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "ConicalGearRating":
            return self._parent

        def __getattr__(self: "ConicalGearRating._Cast_ConicalGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def convex_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearRating._Cast_ConicalGearRating":
        return self._Cast_ConicalGearRating(self)
