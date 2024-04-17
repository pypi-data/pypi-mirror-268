"""ISO63362019MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362019_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63362019MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _523, _521
    from mastapy.gears.rating.cylindrical import _470
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO63362019MeshSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63362019MeshSingleFlankRating")


class ISO63362019MeshSingleFlankRating(_517.ISO63362006MeshSingleFlankRating):
    """ISO63362019MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362019_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63362019MeshSingleFlankRating")

    class _Cast_ISO63362019MeshSingleFlankRating:
        """Special nested class for casting ISO63362019MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
            parent: "ISO63362019MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "_517.ISO63362006MeshSingleFlankRating":
            return self._parent._cast(_517.ISO63362006MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "_523.ISO6336AbstractMetalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _521

            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
        ) -> "ISO63362019MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63362019MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometryFactor

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(
        self: Self,
    ) -> "ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating":
        return self._Cast_ISO63362019MeshSingleFlankRating(self)
