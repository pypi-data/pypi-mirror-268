"""LoadedCylindricalRollerBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2032
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedCylindricalRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2016, _2029, _2037, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingRow")


class LoadedCylindricalRollerBearingRow(_2032.LoadedNonBarrelRollerBearingRow):
    """LoadedCylindricalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedCylindricalRollerBearingRow")

    class _Cast_LoadedCylindricalRollerBearingRow:
        """Special nested class for casting LoadedCylindricalRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
            parent: "LoadedCylindricalRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
        ) -> "_2032.LoadedNonBarrelRollerBearingRow":
            return self._parent._cast(_2032.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
        ) -> "_2029.LoadedNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedNeedleRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
        ) -> "LoadedCylindricalRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow",
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
        self: Self, instance_to_wrap: "LoadedCylindricalRollerBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2016.LoadedCylindricalRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedCylindricalRollerBearingResults

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
    ) -> "LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow":
        return self._Cast_LoadedCylindricalRollerBearingRow(self)
