"""LoadedSphericalRollerThrustBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2036
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerThrustBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2040
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerThrustBearingResults",)


Self = TypeVar("Self", bound="LoadedSphericalRollerThrustBearingResults")


class LoadedSphericalRollerThrustBearingResults(_2036.LoadedRollerBearingResults):
    """LoadedSphericalRollerThrustBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerThrustBearingResults"
    )

    class _Cast_LoadedSphericalRollerThrustBearingResults:
        """Special nested class for casting LoadedSphericalRollerThrustBearingResults to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
            parent: "LoadedSphericalRollerThrustBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_2036.LoadedRollerBearingResults":
            return self._parent._cast(_2036.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_2040.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
        ) -> "LoadedSphericalRollerThrustBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerThrustBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults":
        return self._Cast_LoadedSphericalRollerThrustBearingResults(self)
