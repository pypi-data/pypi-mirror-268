"""LoadedCylindricalRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2031
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedCylindricalRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2071, _2028, _2036, _2040
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingResults")


class LoadedCylindricalRollerBearingResults(_2031.LoadedNonBarrelRollerBearingResults):
    """LoadedCylindricalRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedCylindricalRollerBearingResults"
    )

    class _Cast_LoadedCylindricalRollerBearingResults:
        """Special nested class for casting LoadedCylindricalRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
            parent: "LoadedCylindricalRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_2031.LoadedNonBarrelRollerBearingResults":
            return self._parent._cast(_2031.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_2036.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2036

            return self._parent._cast(_2036.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_2040.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "_2028.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedNeedleRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "LoadedCylindricalRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedCylindricalRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_continuous_axial_load(
        self: Self,
    ) -> "_2071.PermissibleContinuousAxialLoadResults":
        """mastapy.bearings.bearing_results.rolling.PermissibleContinuousAxialLoadResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContinuousAxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults":
        return self._Cast_LoadedCylindricalRollerBearingResults(self)
