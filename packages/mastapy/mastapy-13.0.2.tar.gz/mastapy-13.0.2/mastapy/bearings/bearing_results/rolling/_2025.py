"""LoadedFourPointContactBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedFourPointContactBallBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2024, _2023, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFourPointContactBallBearingRow",)


Self = TypeVar("Self", bound="LoadedFourPointContactBallBearingRow")


class LoadedFourPointContactBallBearingRow(_2010.LoadedBallBearingRow):
    """LoadedFourPointContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedFourPointContactBallBearingRow")

    class _Cast_LoadedFourPointContactBallBearingRow:
        """Special nested class for casting LoadedFourPointContactBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow",
            parent: "LoadedFourPointContactBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(
            self: "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(
            self: "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow",
        ) -> "LoadedFourPointContactBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow",
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
        self: Self, instance_to_wrap: "LoadedFourPointContactBallBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2024.LoadedFourPointContactBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedFourPointContactBallBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def race_results(
        self: Self,
    ) -> "List[_2023.LoadedFourPointContactBallBearingRaceResults]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedFourPointContactBallBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow":
        return self._Cast_LoadedFourPointContactBallBearingRow(self)
