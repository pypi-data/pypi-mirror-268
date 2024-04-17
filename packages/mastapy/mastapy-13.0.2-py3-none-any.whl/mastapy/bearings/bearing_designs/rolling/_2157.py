"""DeepGrooveBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEEP_GROOVE_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "DeepGrooveBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("DeepGrooveBallBearing",)


Self = TypeVar("Self", bound="DeepGrooveBallBearing")


class DeepGrooveBallBearing(_2147.BallBearing):
    """DeepGrooveBallBearing

    This is a mastapy class.
    """

    TYPE = _DEEP_GROOVE_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DeepGrooveBallBearing")

    class _Cast_DeepGrooveBallBearing:
        """Special nested class for casting DeepGrooveBallBearing to subclasses."""

        def __init__(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
            parent: "DeepGrooveBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2147.BallBearing":
            return self._parent._cast(_2147.BallBearing)

        @property
        def rolling_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def deep_groove_ball_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "DeepGrooveBallBearing":
            return self._parent

        def __getattr__(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DeepGrooveBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing":
        return self._Cast_DeepGrooveBallBearing(self)
