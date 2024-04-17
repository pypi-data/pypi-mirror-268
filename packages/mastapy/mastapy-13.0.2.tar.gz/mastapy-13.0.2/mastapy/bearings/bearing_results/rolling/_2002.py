"""LoadedAxialThrustCylindricalRollerBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2032
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustCylindricalRollerBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2001, _2005, _2037, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustCylindricalRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedAxialThrustCylindricalRollerBearingRow")


class LoadedAxialThrustCylindricalRollerBearingRow(
    _2032.LoadedNonBarrelRollerBearingRow
):
    """LoadedAxialThrustCylindricalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustCylindricalRollerBearingRow"
    )

    class _Cast_LoadedAxialThrustCylindricalRollerBearingRow:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
            parent: "LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "_2032.LoadedNonBarrelRollerBearingRow":
            return self._parent._cast(_2032.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "_2005.LoadedAxialThrustNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(_2005.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "LoadedAxialThrustCylindricalRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
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
        instance_to_wrap: "LoadedAxialThrustCylindricalRollerBearingRow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(
        self: Self,
    ) -> "_2001.LoadedAxialThrustCylindricalRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedAxialThrustCylindricalRollerBearingResults

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
    ) -> "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow":
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingRow(self)
