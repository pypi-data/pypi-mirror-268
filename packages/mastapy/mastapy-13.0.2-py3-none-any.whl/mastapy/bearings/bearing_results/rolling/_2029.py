"""LoadedNeedleRollerBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2017
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NEEDLE_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNeedleRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2028, _2032, _2037, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNeedleRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedNeedleRollerBearingRow")


class LoadedNeedleRollerBearingRow(_2017.LoadedCylindricalRollerBearingRow):
    """LoadedNeedleRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_NEEDLE_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNeedleRollerBearingRow")

    class _Cast_LoadedNeedleRollerBearingRow:
        """Special nested class for casting LoadedNeedleRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
            parent: "LoadedNeedleRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
        ) -> "_2017.LoadedCylindricalRollerBearingRow":
            return self._parent._cast(_2017.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
        ) -> "_2032.LoadedNonBarrelRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
        ) -> "LoadedNeedleRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNeedleRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cage_land_sliding_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CageLandSlidingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_power_loss_traction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_power_loss_traction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss_traction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self: Self) -> "_2028.LoadedNeedleRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedNeedleRollerBearingResults

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
    ) -> "LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow":
        return self._Cast_LoadedNeedleRollerBearingRow(self)
