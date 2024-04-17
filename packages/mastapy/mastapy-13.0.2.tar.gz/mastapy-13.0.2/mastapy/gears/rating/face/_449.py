"""FaceGearMeshDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearMeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshDutyCycleRating",)


Self = TypeVar("Self", bound="FaceGearMeshDutyCycleRating")


class FaceGearMeshDutyCycleRating(_368.MeshDutyCycleRating):
    """FaceGearMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshDutyCycleRating")

    class _Cast_FaceGearMeshDutyCycleRating:
        """Special nested class for casting FaceGearMeshDutyCycleRating to subclasses."""

        def __init__(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
            parent: "FaceGearMeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
        ) -> "_368.MeshDutyCycleRating":
            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
        ) -> "FaceGearMeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating":
        return self._Cast_FaceGearMeshDutyCycleRating(self)
