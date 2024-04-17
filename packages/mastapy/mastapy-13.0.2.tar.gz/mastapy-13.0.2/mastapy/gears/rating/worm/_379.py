"""WormGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _963
    from mastapy.gears.rating.worm import _377, _376
    from mastapy.gears.rating import _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetRating",)


Self = TypeVar("Self", bound="WormGearSetRating")


class WormGearSetRating(_366.GearSetRating):
    """WormGearSetRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetRating")

    class _Cast_WormGearSetRating:
        """Special nested class for casting WormGearSetRating to subclasses."""

        def __init__(
            self: "WormGearSetRating._Cast_WormGearSetRating",
            parent: "WormGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(
            self: "WormGearSetRating._Cast_WormGearSetRating",
        ) -> "_366.GearSetRating":
            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "WormGearSetRating._Cast_WormGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "WormGearSetRating._Cast_WormGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_rating(
            self: "WormGearSetRating._Cast_WormGearSetRating",
        ) -> "WormGearSetRating":
            return self._parent

        def __getattr__(self: "WormGearSetRating._Cast_WormGearSetRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return ""

        return temp

    @property
    def worm_gear_set(self: Self) -> "_963.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSet

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
    def gear_mesh_ratings(self: Self) -> "List[_376.WormGearMeshRating]":
        """List[mastapy.gears.rating.worm.WormGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_mesh_ratings(self: Self) -> "List[_376.WormGearMeshRating]":
        """List[mastapy.gears.rating.worm.WormGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormGearSetRating._Cast_WormGearSetRating":
        return self._Cast_WormGearSetRating(self)
