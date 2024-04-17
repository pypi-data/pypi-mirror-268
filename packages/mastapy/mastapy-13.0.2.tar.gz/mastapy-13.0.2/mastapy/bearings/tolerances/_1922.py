"""RaceRoundnessAtAngle"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_ROUNDNESS_AT_ANGLE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "RaceRoundnessAtAngle"
)


__docformat__ = "restructuredtext en"
__all__ = ("RaceRoundnessAtAngle",)


Self = TypeVar("Self", bound="RaceRoundnessAtAngle")


class RaceRoundnessAtAngle(_0.APIBase):
    """RaceRoundnessAtAngle

    This is a mastapy class.
    """

    TYPE = _RACE_ROUNDNESS_AT_ANGLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RaceRoundnessAtAngle")

    class _Cast_RaceRoundnessAtAngle:
        """Special nested class for casting RaceRoundnessAtAngle to subclasses."""

        def __init__(
            self: "RaceRoundnessAtAngle._Cast_RaceRoundnessAtAngle",
            parent: "RaceRoundnessAtAngle",
        ):
            self._parent = parent

        @property
        def race_roundness_at_angle(
            self: "RaceRoundnessAtAngle._Cast_RaceRoundnessAtAngle",
        ) -> "RaceRoundnessAtAngle":
            return self._parent

        def __getattr__(
            self: "RaceRoundnessAtAngle._Cast_RaceRoundnessAtAngle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RaceRoundnessAtAngle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "RaceRoundnessAtAngle._Cast_RaceRoundnessAtAngle":
        return self._Cast_RaceRoundnessAtAngle(self)
