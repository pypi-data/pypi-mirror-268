"""LoadedAngularContactThrustBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1991
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactThrustBallBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1993, _2010, _2041


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactThrustBallBearingRow",)


Self = TypeVar("Self", bound="LoadedAngularContactThrustBallBearingRow")


class LoadedAngularContactThrustBallBearingRow(
    _1991.LoadedAngularContactBallBearingRow
):
    """LoadedAngularContactThrustBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactThrustBallBearingRow"
    )

    class _Cast_LoadedAngularContactThrustBallBearingRow:
        """Special nested class for casting LoadedAngularContactThrustBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
            parent: "LoadedAngularContactThrustBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
        ) -> "_1991.LoadedAngularContactBallBearingRow":
            return self._parent._cast(_1991.LoadedAngularContactBallBearingRow)

        @property
        def loaded_ball_bearing_row(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
        ) -> "LoadedAngularContactThrustBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow",
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
        self: Self, instance_to_wrap: "LoadedAngularContactThrustBallBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(
        self: Self,
    ) -> "_1993.LoadedAngularContactThrustBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedAngularContactThrustBallBearingResults

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
    ) -> "LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow":
        return self._Cast_LoadedAngularContactThrustBallBearingRow(self)
