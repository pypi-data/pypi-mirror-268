"""LoadedAngularContactBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedAngularContactBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1990, _1994, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactBallBearingRow",)


Self = TypeVar("Self", bound="LoadedAngularContactBallBearingRow")


class LoadedAngularContactBallBearingRow(_2010.LoadedBallBearingRow):
    """LoadedAngularContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedAngularContactBallBearingRow")

    class _Cast_LoadedAngularContactBallBearingRow:
        """Special nested class for casting LoadedAngularContactBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
            parent: "LoadedAngularContactBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
        ) -> "_1994.LoadedAngularContactThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(_1994.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
        ) -> "LoadedAngularContactBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow",
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
        self: Self, instance_to_wrap: "LoadedAngularContactBallBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_1990.LoadedAngularContactBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedAngularContactBallBearingResults

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
    ) -> "LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow":
        return self._Cast_LoadedAngularContactBallBearingRow(self)
