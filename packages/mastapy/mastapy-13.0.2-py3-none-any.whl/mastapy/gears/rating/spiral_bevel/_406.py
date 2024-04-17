"""SpiralBevelGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.SpiralBevel", "SpiralBevelGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.rating.agma_gleason_conical import _569
    from mastapy.gears.rating.conical import _543
    from mastapy.gears.rating import _364, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearRating",)


Self = TypeVar("Self", bound="SpiralBevelGearRating")


class SpiralBevelGearRating(_558.BevelGearRating):
    """SpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearRating")

    class _Cast_SpiralBevelGearRating:
        """Special nested class for casting SpiralBevelGearRating to subclasses."""

        def __init__(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
            parent: "SpiralBevelGearRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_558.BevelGearRating":
            return self._parent._cast(_558.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_569.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _569

            return self._parent._cast(_569.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_543.ConicalGearRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearRating)

        @property
        def gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def spiral_bevel_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "SpiralBevelGearRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear(self: Self) -> "_973.SpiralBevelGearDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpiralBevelGearRating._Cast_SpiralBevelGearRating":
        return self._Cast_SpiralBevelGearRating(self)
