"""RoundedOrder"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUNDED_ORDER = python_net_import("SMT.MastaAPI.MathUtility", "RoundedOrder")


__docformat__ = "restructuredtext en"
__all__ = ("RoundedOrder",)


Self = TypeVar("Self", bound="RoundedOrder")


class RoundedOrder(_0.APIBase):
    """RoundedOrder

    This is a mastapy class.
    """

    TYPE = _ROUNDED_ORDER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RoundedOrder")

    class _Cast_RoundedOrder:
        """Special nested class for casting RoundedOrder to subclasses."""

        def __init__(self: "RoundedOrder._Cast_RoundedOrder", parent: "RoundedOrder"):
            self._parent = parent

        @property
        def rounded_order(self: "RoundedOrder._Cast_RoundedOrder") -> "RoundedOrder":
            return self._parent

        def __getattr__(self: "RoundedOrder._Cast_RoundedOrder", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RoundedOrder.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RoundedOrder._Cast_RoundedOrder":
        return self._Cast_RoundedOrder(self)
