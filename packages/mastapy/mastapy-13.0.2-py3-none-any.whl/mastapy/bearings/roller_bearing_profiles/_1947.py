"""UserSpecifiedRollerRaceProfilePoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.roller_bearing_profiles import _1945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_SPECIFIED_ROLLER_RACE_PROFILE_POINT = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "UserSpecifiedRollerRaceProfilePoint"
)


__docformat__ = "restructuredtext en"
__all__ = ("UserSpecifiedRollerRaceProfilePoint",)


Self = TypeVar("Self", bound="UserSpecifiedRollerRaceProfilePoint")


class UserSpecifiedRollerRaceProfilePoint(_1945.RollerRaceProfilePoint):
    """UserSpecifiedRollerRaceProfilePoint

    This is a mastapy class.
    """

    TYPE = _USER_SPECIFIED_ROLLER_RACE_PROFILE_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UserSpecifiedRollerRaceProfilePoint")

    class _Cast_UserSpecifiedRollerRaceProfilePoint:
        """Special nested class for casting UserSpecifiedRollerRaceProfilePoint to subclasses."""

        def __init__(
            self: "UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint",
            parent: "UserSpecifiedRollerRaceProfilePoint",
        ):
            self._parent = parent

        @property
        def roller_race_profile_point(
            self: "UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint",
        ) -> "_1945.RollerRaceProfilePoint":
            return self._parent._cast(_1945.RollerRaceProfilePoint)

        @property
        def user_specified_roller_race_profile_point(
            self: "UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint",
        ) -> "UserSpecifiedRollerRaceProfilePoint":
            return self._parent

        def __getattr__(
            self: "UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint",
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
        self: Self, instance_to_wrap: "UserSpecifiedRollerRaceProfilePoint.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def race_deviation_used_in_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceDeviationUsedInAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def roller_deviation_used_in_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollerDeviationUsedInAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> (
        "UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint"
    ):
        return self._Cast_UserSpecifiedRollerRaceProfilePoint(self)
