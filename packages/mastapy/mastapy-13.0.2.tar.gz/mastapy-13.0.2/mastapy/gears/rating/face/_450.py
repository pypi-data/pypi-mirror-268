"""FaceGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _329
    from mastapy.gears.gear_designs.face import _995
    from mastapy.gears.rating.face import _453, _451
    from mastapy.gears.load_case.face import _884
    from mastapy.gears.rating.cylindrical.iso6336 import _517
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshRating",)


Self = TypeVar("Self", bound="FaceGearMeshRating")


class FaceGearMeshRating(_363.GearMeshRating):
    """FaceGearMeshRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshRating")

    class _Cast_FaceGearMeshRating:
        """Special nested class for casting FaceGearMeshRating to subclasses."""

        def __init__(
            self: "FaceGearMeshRating._Cast_FaceGearMeshRating",
            parent: "FaceGearMeshRating",
        ):
            self._parent = parent

        @property
        def gear_mesh_rating(
            self: "FaceGearMeshRating._Cast_FaceGearMeshRating",
        ) -> "_363.GearMeshRating":
            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "FaceGearMeshRating._Cast_FaceGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "FaceGearMeshRating._Cast_FaceGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def face_gear_mesh_rating(
            self: "FaceGearMeshRating._Cast_FaceGearMeshRating",
        ) -> "FaceGearMeshRating":
            return self._parent

        def __getattr__(self: "FaceGearMeshRating._Cast_FaceGearMeshRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_329.GearFlanks":
        """mastapy.gears.GearFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.GearFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._329", "GearFlanks")(value)

    @property
    def face_gear_mesh(self: Self) -> "_995.FaceGearMeshDesign":
        """mastapy.gears.gear_designs.face.FaceGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_rating(self: Self) -> "_453.FaceGearSetRating":
        """mastapy.gears.rating.face.FaceGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_load_case(self: Self) -> "_884.FaceMeshLoadCase":
        """mastapy.gears.load_case.face.FaceMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_single_flank_rating(self: Self) -> "_517.ISO63362006MeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.iso6336.ISO63362006MeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "FaceGearMeshRating._Cast_FaceGearMeshRating":
        return self._Cast_FaceGearMeshRating(self)
