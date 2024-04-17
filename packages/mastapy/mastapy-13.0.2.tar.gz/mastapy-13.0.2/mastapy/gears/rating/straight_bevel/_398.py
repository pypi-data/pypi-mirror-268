"""StraightBevelGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _557
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevel", "StraightBevelGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _966
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.gears.rating.agma_gleason_conical import _568
    from mastapy.gears.rating.conical import _542
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshRating",)


Self = TypeVar("Self", bound="StraightBevelGearMeshRating")


class StraightBevelGearMeshRating(_557.BevelGearMeshRating):
    """StraightBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMeshRating")

    class _Cast_StraightBevelGearMeshRating:
        """Special nested class for casting StraightBevelGearMeshRating to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
            parent: "StraightBevelGearMeshRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_557.BevelGearMeshRating":
            return self._parent._cast(_557.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_568.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _568

            return self._parent._cast(_568.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
        ) -> "StraightBevelGearMeshRating":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_mesh(self: Self) -> "_966.StraightBevelGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_ratings(self: Self) -> "List[_399.StraightBevelGearRating]":
        """List[mastapy.gears.rating.straight_bevel.StraightBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating":
        return self._Cast_StraightBevelGearMeshRating(self)
