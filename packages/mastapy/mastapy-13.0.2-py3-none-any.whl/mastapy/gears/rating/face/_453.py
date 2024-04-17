"""FaceGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999
    from mastapy.gears.rating.face import _451, _450
    from mastapy.gears.rating import _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetRating",)


Self = TypeVar("Self", bound="FaceGearSetRating")


class FaceGearSetRating(_366.GearSetRating):
    """FaceGearSetRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetRating")

    class _Cast_FaceGearSetRating:
        """Special nested class for casting FaceGearSetRating to subclasses."""

        def __init__(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
            parent: "FaceGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ) -> "_366.GearSetRating":
            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def face_gear_set_rating(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ) -> "FaceGearSetRating":
            return self._parent

        def __getattr__(self: "FaceGearSetRating._Cast_FaceGearSetRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetRating.TYPE"):
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
    def face_gear_set(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_451.FaceGearRating]":
        """List[mastapy.gears.rating.face.FaceGearRating]

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
    def face_gear_ratings(self: Self) -> "List[_451.FaceGearRating]":
        """List[mastapy.gears.rating.face.FaceGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: Self) -> "List[_450.FaceGearMeshRating]":
        """List[mastapy.gears.rating.face.FaceGearMeshRating]

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
    def face_mesh_ratings(self: Self) -> "List[_450.FaceGearMeshRating]":
        """List[mastapy.gears.rating.face.FaceGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetRating._Cast_FaceGearSetRating":
        return self._Cast_FaceGearSetRating(self)
