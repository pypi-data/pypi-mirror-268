"""LoadedThrustBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THRUST_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedThrustBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2061, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedThrustBallBearingRow",)


Self = TypeVar("Self", bound="LoadedThrustBallBearingRow")


class LoadedThrustBallBearingRow(_2010.LoadedBallBearingRow):
    """LoadedThrustBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_THRUST_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedThrustBallBearingRow")

    class _Cast_LoadedThrustBallBearingRow:
        """Special nested class for casting LoadedThrustBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow",
            parent: "LoadedThrustBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(
            self: "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(
            self: "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow",
        ) -> "LoadedThrustBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedThrustBallBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2061.LoadedThrustBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedThrustBallBearingResults

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
    ) -> "LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow":
        return self._Cast_LoadedThrustBallBearingRow(self)
