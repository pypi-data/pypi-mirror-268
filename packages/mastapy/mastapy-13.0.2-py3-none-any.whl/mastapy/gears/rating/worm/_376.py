"""WormGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _962
    from mastapy.gears.rating.worm import _377
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshRating",)


Self = TypeVar("Self", bound="WormGearMeshRating")


class WormGearMeshRating(_363.GearMeshRating):
    """WormGearMeshRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshRating")

    class _Cast_WormGearMeshRating:
        """Special nested class for casting WormGearMeshRating to subclasses."""

        def __init__(
            self: "WormGearMeshRating._Cast_WormGearMeshRating",
            parent: "WormGearMeshRating",
        ):
            self._parent = parent

        @property
        def gear_mesh_rating(
            self: "WormGearMeshRating._Cast_WormGearMeshRating",
        ) -> "_363.GearMeshRating":
            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "WormGearMeshRating._Cast_WormGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "WormGearMeshRating._Cast_WormGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def worm_gear_mesh_rating(
            self: "WormGearMeshRating._Cast_WormGearMeshRating",
        ) -> "WormGearMeshRating":
            return self._parent

        def __getattr__(self: "WormGearMeshRating._Cast_WormGearMeshRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_gear_mesh(self: Self) -> "_962.WormGearMeshDesign":
        """mastapy.gears.gear_designs.worm.WormGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "WormGearMeshRating._Cast_WormGearMeshRating":
        return self._Cast_WormGearMeshRating(self)
