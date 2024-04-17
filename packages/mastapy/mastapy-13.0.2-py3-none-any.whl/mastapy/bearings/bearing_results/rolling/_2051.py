"""LoadedSphericalRollerThrustBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_THRUST_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerThrustBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2050, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerThrustBearingRow",)


Self = TypeVar("Self", bound="LoadedSphericalRollerThrustBearingRow")


class LoadedSphericalRollerThrustBearingRow(_2037.LoadedRollerBearingRow):
    """LoadedSphericalRollerThrustBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_THRUST_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerThrustBearingRow"
    )

    class _Cast_LoadedSphericalRollerThrustBearingRow:
        """Special nested class for casting LoadedSphericalRollerThrustBearingRow to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow",
            parent: "LoadedSphericalRollerThrustBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(
            self: "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(
            self: "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow",
        ) -> "LoadedSphericalRollerThrustBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerThrustBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2050.LoadedSphericalRollerThrustBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedSphericalRollerThrustBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRollerThrustBearingRow._Cast_LoadedSphericalRollerThrustBearingRow":
        return self._Cast_LoadedSphericalRollerThrustBearingRow(self)
