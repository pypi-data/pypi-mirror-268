"""AngularContactThrustBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs.rolling import _2142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_THRUST_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AngularContactThrustBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2147, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("AngularContactThrustBallBearing",)


Self = TypeVar("Self", bound="AngularContactThrustBallBearing")


class AngularContactThrustBallBearing(_2142.AngularContactBallBearing):
    """AngularContactThrustBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_THRUST_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularContactThrustBallBearing")

    class _Cast_AngularContactThrustBallBearing:
        """Special nested class for casting AngularContactThrustBallBearing to subclasses."""

        def __init__(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
            parent: "AngularContactThrustBallBearing",
        ):
            self._parent = parent

        @property
        def angular_contact_ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2142.AngularContactBallBearing":
            return self._parent._cast(_2142.AngularContactBallBearing)

        @property
        def ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2147.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.BallBearing)

        @property
        def rolling_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "AngularContactThrustBallBearing":
            return self._parent

        def __getattr__(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularContactThrustBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing":
        return self._Cast_AngularContactThrustBallBearing(self)
