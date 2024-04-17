"""LoadedSphericalRollerRadialBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerRadialBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2047, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerRadialBearingRow",)


Self = TypeVar("Self", bound="LoadedSphericalRollerRadialBearingRow")


class LoadedSphericalRollerRadialBearingRow(_2037.LoadedRollerBearingRow):
    """LoadedSphericalRollerRadialBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerRadialBearingRow"
    )

    class _Cast_LoadedSphericalRollerRadialBearingRow:
        """Special nested class for casting LoadedSphericalRollerRadialBearingRow to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow",
            parent: "LoadedSphericalRollerRadialBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(
            self: "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(
            self: "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow",
        ) -> "LoadedSphericalRollerRadialBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerRadialBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2047.LoadedSphericalRollerRadialBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedSphericalRollerRadialBearingResults

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
    ) -> "LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow":
        return self._Cast_LoadedSphericalRollerRadialBearingRow(self)
