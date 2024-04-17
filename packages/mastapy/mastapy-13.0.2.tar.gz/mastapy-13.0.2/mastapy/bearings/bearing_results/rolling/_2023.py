"""LoadedFourPointContactBallBearingRaceResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2008
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RACE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedFourPointContactBallBearingRaceResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2039


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFourPointContactBallBearingRaceResults",)


Self = TypeVar("Self", bound="LoadedFourPointContactBallBearingRaceResults")


class LoadedFourPointContactBallBearingRaceResults(_2008.LoadedBallBearingRaceResults):
    """LoadedFourPointContactBallBearingRaceResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RACE_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedFourPointContactBallBearingRaceResults"
    )

    class _Cast_LoadedFourPointContactBallBearingRaceResults:
        """Special nested class for casting LoadedFourPointContactBallBearingRaceResults to subclasses."""

        def __init__(
            self: "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults",
            parent: "LoadedFourPointContactBallBearingRaceResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_race_results(
            self: "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults",
        ) -> "_2008.LoadedBallBearingRaceResults":
            return self._parent._cast(_2008.LoadedBallBearingRaceResults)

        @property
        def loaded_rolling_bearing_race_results(
            self: "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults",
        ) -> "_2039.LoadedRollingBearingRaceResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedRollingBearingRaceResults)

        @property
        def loaded_four_point_contact_ball_bearing_race_results(
            self: "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults",
        ) -> "LoadedFourPointContactBallBearingRaceResults":
            return self._parent

        def __getattr__(
            self: "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults",
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
        self: Self,
        instance_to_wrap: "LoadedFourPointContactBallBearingRaceResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults":
        return self._Cast_LoadedFourPointContactBallBearingRaceResults(self)
