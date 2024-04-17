"""RollerRaceProfilePoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_RACE_PROFILE_POINT = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerRaceProfilePoint"
)

if TYPE_CHECKING:
    from mastapy.bearings.roller_bearing_profiles import _1947


__docformat__ = "restructuredtext en"
__all__ = ("RollerRaceProfilePoint",)


Self = TypeVar("Self", bound="RollerRaceProfilePoint")


class RollerRaceProfilePoint(_0.APIBase):
    """RollerRaceProfilePoint

    This is a mastapy class.
    """

    TYPE = _ROLLER_RACE_PROFILE_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerRaceProfilePoint")

    class _Cast_RollerRaceProfilePoint:
        """Special nested class for casting RollerRaceProfilePoint to subclasses."""

        def __init__(
            self: "RollerRaceProfilePoint._Cast_RollerRaceProfilePoint",
            parent: "RollerRaceProfilePoint",
        ):
            self._parent = parent

        @property
        def user_specified_roller_race_profile_point(
            self: "RollerRaceProfilePoint._Cast_RollerRaceProfilePoint",
        ) -> "_1947.UserSpecifiedRollerRaceProfilePoint":
            from mastapy.bearings.roller_bearing_profiles import _1947

            return self._parent._cast(_1947.UserSpecifiedRollerRaceProfilePoint)

        @property
        def roller_race_profile_point(
            self: "RollerRaceProfilePoint._Cast_RollerRaceProfilePoint",
        ) -> "RollerRaceProfilePoint":
            return self._parent

        def __getattr__(
            self: "RollerRaceProfilePoint._Cast_RollerRaceProfilePoint", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerRaceProfilePoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_from_roller_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetFromRollerCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def race_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def roller_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollerDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def total_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "RollerRaceProfilePoint._Cast_RollerRaceProfilePoint":
        return self._Cast_RollerRaceProfilePoint(self)
