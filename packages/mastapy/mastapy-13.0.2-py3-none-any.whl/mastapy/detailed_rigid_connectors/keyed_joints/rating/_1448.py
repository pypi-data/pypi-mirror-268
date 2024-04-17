"""KeywayHalfRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.Rating", "KeywayHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("KeywayHalfRating",)


Self = TypeVar("Self", bound="KeywayHalfRating")


class KeywayHalfRating(_0.APIBase):
    """KeywayHalfRating

    This is a mastapy class.
    """

    TYPE = _KEYWAY_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KeywayHalfRating")

    class _Cast_KeywayHalfRating:
        """Special nested class for casting KeywayHalfRating to subclasses."""

        def __init__(
            self: "KeywayHalfRating._Cast_KeywayHalfRating", parent: "KeywayHalfRating"
        ):
            self._parent = parent

        @property
        def keyway_half_rating(
            self: "KeywayHalfRating._Cast_KeywayHalfRating",
        ) -> "KeywayHalfRating":
            return self._parent

        def __getattr__(self: "KeywayHalfRating._Cast_KeywayHalfRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KeywayHalfRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "KeywayHalfRating._Cast_KeywayHalfRating":
        return self._Cast_KeywayHalfRating(self)
