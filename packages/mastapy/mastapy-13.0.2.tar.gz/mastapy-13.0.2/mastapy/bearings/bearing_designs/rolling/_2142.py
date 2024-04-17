"""AngularContactBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AngularContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2143, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("AngularContactBallBearing",)


Self = TypeVar("Self", bound="AngularContactBallBearing")


class AngularContactBallBearing(_2147.BallBearing):
    """AngularContactBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularContactBallBearing")

    class _Cast_AngularContactBallBearing:
        """Special nested class for casting AngularContactBallBearing to subclasses."""

        def __init__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
            parent: "AngularContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2147.BallBearing":
            return self._parent._cast(_2147.BallBearing)

        @property
        def rolling_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2143.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2143

            return self._parent._cast(_2143.AngularContactThrustBallBearing)

        @property
        def angular_contact_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "AngularContactBallBearing":
            return self._parent

        def __getattr__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AngularContactBallBearing._Cast_AngularContactBallBearing":
        return self._Cast_AngularContactBallBearing(self)
