"""FaceGearDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearDutyCycleRating",)


Self = TypeVar("Self", bound="FaceGearDutyCycleRating")


class FaceGearDutyCycleRating(_361.GearDutyCycleRating):
    """FaceGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearDutyCycleRating")

    class _Cast_FaceGearDutyCycleRating:
        """Special nested class for casting FaceGearDutyCycleRating to subclasses."""

        def __init__(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating",
            parent: "FaceGearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating",
        ) -> "_361.GearDutyCycleRating":
            return self._parent._cast(_361.GearDutyCycleRating)

        @property
        def abstract_gear_rating(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def face_gear_duty_cycle_rating(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating",
        ) -> "FaceGearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearDutyCycleRating._Cast_FaceGearDutyCycleRating":
        return self._Cast_FaceGearDutyCycleRating(self)
