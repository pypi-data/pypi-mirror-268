"""FaceGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _993
    from mastapy.gears.rating import _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearRating",)


Self = TypeVar("Self", bound="FaceGearRating")


class FaceGearRating(_364.GearRating):
    """FaceGearRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearRating")

    class _Cast_FaceGearRating:
        """Special nested class for casting FaceGearRating to subclasses."""

        def __init__(
            self: "FaceGearRating._Cast_FaceGearRating", parent: "FaceGearRating"
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "FaceGearRating._Cast_FaceGearRating",
        ) -> "_364.GearRating":
            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "FaceGearRating._Cast_FaceGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "FaceGearRating._Cast_FaceGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def face_gear_rating(
            self: "FaceGearRating._Cast_FaceGearRating",
        ) -> "FaceGearRating":
            return self._parent

        def __getattr__(self: "FaceGearRating._Cast_FaceGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear(self: Self) -> "_993.FaceGearDesign":
        """mastapy.gears.gear_designs.face.FaceGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearRating._Cast_FaceGearRating":
        return self._Cast_FaceGearRating(self)
