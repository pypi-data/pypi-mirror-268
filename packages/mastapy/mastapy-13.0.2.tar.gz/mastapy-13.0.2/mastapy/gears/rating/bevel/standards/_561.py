"""AGMASpiralBevelMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.implicit import overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel.standards import _565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards", "AGMASpiralBevelMeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel.standards import _560
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("AGMASpiralBevelMeshSingleFlankRating",)


Self = TypeVar("Self", bound="AGMASpiralBevelMeshSingleFlankRating")


class AGMASpiralBevelMeshSingleFlankRating(_565.SpiralBevelMeshSingleFlankRating):
    """AGMASpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMASpiralBevelMeshSingleFlankRating")

    class _Cast_AGMASpiralBevelMeshSingleFlankRating:
        """Special nested class for casting AGMASpiralBevelMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
            parent: "AGMASpiralBevelMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
        ) -> "_565.SpiralBevelMeshSingleFlankRating":
            return self._parent._cast(_565.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
        ) -> "AGMASpiralBevelMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "AGMASpiralBevelMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrowningFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_560.AGMASpiralBevelGearSingleFlankRating]":
        """List[mastapy.gears.rating.bevel.standards.AGMASpiralBevelGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_bevel_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_560.AGMASpiralBevelGearSingleFlankRating]":
        """List[mastapy.gears.rating.bevel.standards.AGMASpiralBevelGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMABevelGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMASpiralBevelMeshSingleFlankRating._Cast_AGMASpiralBevelMeshSingleFlankRating":
        return self._Cast_AGMASpiralBevelMeshSingleFlankRating(self)
