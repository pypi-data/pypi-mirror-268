"""LoadedTaperRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2031
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedTaperRollerBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2036, _2040
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTaperRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedTaperRollerBearingResults")


class LoadedTaperRollerBearingResults(_2031.LoadedNonBarrelRollerBearingResults):
    """LoadedTaperRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTaperRollerBearingResults")

    class _Cast_LoadedTaperRollerBearingResults:
        """Special nested class for casting LoadedTaperRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
            parent: "LoadedTaperRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_2031.LoadedNonBarrelRollerBearingResults":
            return self._parent._cast(_2031.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_2036.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2036

            return self._parent._cast(_2036.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_2040.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "LoadedTaperRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedTaperRollerBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults":
        return self._Cast_LoadedTaperRollerBearingResults(self)
