"""ZerolBevelGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _559
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.ZerolBevel", "ZerolBevelGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _958
    from mastapy.gears.rating.zerol_bevel import _373, _372
    from mastapy.gears.rating.agma_gleason_conical import _570
    from mastapy.gears.rating.conical import _545
    from mastapy.gears.rating import _366, _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetRating",)


Self = TypeVar("Self", bound="ZerolBevelGearSetRating")


class ZerolBevelGearSetRating(_559.BevelGearSetRating):
    """ZerolBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetRating")

    class _Cast_ZerolBevelGearSetRating:
        """Special nested class for casting ZerolBevelGearSetRating to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
            parent: "ZerolBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_559.BevelGearSetRating":
            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_570.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _570

            return self._parent._cast(_570.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_545.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_366.GearSetRating":
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "ZerolBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self: Self) -> "_958.ZerolBevelGearSetDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_ratings(self: Self) -> "List[_373.ZerolBevelGearRating]":
        """List[mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_mesh_ratings(self: Self) -> "List[_372.ZerolBevelGearMeshRating]":
        """List[mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating":
        return self._Cast_ZerolBevelGearSetRating(self)
