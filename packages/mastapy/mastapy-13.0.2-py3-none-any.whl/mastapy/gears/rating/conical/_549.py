"""ConicalMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalMeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _425, _426, _427, _428, _429
    from mastapy.gears.rating.hypoid.standards import _446
    from mastapy.gears.rating.bevel.standards import _561, _563, _565


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshSingleFlankRating",)


Self = TypeVar("Self", bound="ConicalMeshSingleFlankRating")


class ConicalMeshSingleFlankRating(_369.MeshSingleFlankRating):
    """ConicalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshSingleFlankRating")

    class _Cast_ConicalMeshSingleFlankRating:
        """Special nested class for casting ConicalMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
            parent: "ConicalMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_425.ISO10300MeshSingleFlankRating":
            from mastapy.gears.rating.iso_10300 import _425

            return self._parent._cast(_425.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_426.ISO10300MeshSingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _426

            return self._parent._cast(_426.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_427.ISO10300MeshSingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _427

            return self._parent._cast(_427.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_428.ISO10300MeshSingleFlankRatingMethodB1":
            from mastapy.gears.rating.iso_10300 import _428

            return self._parent._cast(_428.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_429.ISO10300MeshSingleFlankRatingMethodB2":
            from mastapy.gears.rating.iso_10300 import _429

            return self._parent._cast(_429.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_446.GleasonHypoidMeshSingleFlankRating":
            from mastapy.gears.rating.hypoid.standards import _446

            return self._parent._cast(_446.GleasonHypoidMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_561.AGMASpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _561

            return self._parent._cast(_561.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_563.GleasonSpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _563

            return self._parent._cast(_563.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "_565.SpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _565

            return self._parent._cast(_565.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "ConicalMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating":
        return self._Cast_ConicalMeshSingleFlankRating(self)
