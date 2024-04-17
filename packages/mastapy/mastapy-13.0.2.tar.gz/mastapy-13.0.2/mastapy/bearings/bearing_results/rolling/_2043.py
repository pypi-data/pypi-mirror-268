"""LoadedSelfAligningBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2009
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SELF_ALIGNING_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSelfAligningBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2040
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSelfAligningBallBearingResults",)


Self = TypeVar("Self", bound="LoadedSelfAligningBallBearingResults")


class LoadedSelfAligningBallBearingResults(_2009.LoadedBallBearingResults):
    """LoadedSelfAligningBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SELF_ALIGNING_BALL_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedSelfAligningBallBearingResults")

    class _Cast_LoadedSelfAligningBallBearingResults:
        """Special nested class for casting LoadedSelfAligningBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
            parent: "LoadedSelfAligningBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_2009.LoadedBallBearingResults":
            return self._parent._cast(_2009.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_2040.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
        ) -> "LoadedSelfAligningBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedSelfAligningBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults":
        return self._Cast_LoadedSelfAligningBallBearingResults(self)
