"""NamedPoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_POINT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles", "NamedPoint"
)


__docformat__ = "restructuredtext en"
__all__ = ("NamedPoint",)


Self = TypeVar("Self", bound="NamedPoint")


class NamedPoint(_0.APIBase):
    """NamedPoint

    This is a mastapy class.
    """

    TYPE = _NAMED_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedPoint")

    class _Cast_NamedPoint:
        """Special nested class for casting NamedPoint to subclasses."""

        def __init__(self: "NamedPoint._Cast_NamedPoint", parent: "NamedPoint"):
            self._parent = parent

        @property
        def named_point(self: "NamedPoint._Cast_NamedPoint") -> "NamedPoint":
            return self._parent

        def __getattr__(self: "NamedPoint._Cast_NamedPoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @property
    def y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "NamedPoint._Cast_NamedPoint":
        return self._Cast_NamedPoint(self)
