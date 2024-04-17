"""DIN5466SplineHalfRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5466_SPLINE_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "DIN5466SplineHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("DIN5466SplineHalfRating",)


Self = TypeVar("Self", bound="DIN5466SplineHalfRating")


class DIN5466SplineHalfRating(_1438.SplineHalfRating):
    """DIN5466SplineHalfRating

    This is a mastapy class.
    """

    TYPE = _DIN5466_SPLINE_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN5466SplineHalfRating")

    class _Cast_DIN5466SplineHalfRating:
        """Special nested class for casting DIN5466SplineHalfRating to subclasses."""

        def __init__(
            self: "DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating",
            parent: "DIN5466SplineHalfRating",
        ):
            self._parent = parent

        @property
        def spline_half_rating(
            self: "DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating",
        ) -> "_1438.SplineHalfRating":
            return self._parent._cast(_1438.SplineHalfRating)

        @property
        def din5466_spline_half_rating(
            self: "DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating",
        ) -> "DIN5466SplineHalfRating":
            return self._parent

        def __getattr__(
            self: "DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN5466SplineHalfRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating":
        return self._Cast_DIN5466SplineHalfRating(self)
