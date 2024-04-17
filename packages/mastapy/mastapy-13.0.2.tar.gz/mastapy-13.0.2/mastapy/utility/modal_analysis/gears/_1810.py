"""OrderSelector"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_SELECTOR = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "OrderSelector"
)


__docformat__ = "restructuredtext en"
__all__ = ("OrderSelector",)


Self = TypeVar("Self", bound="OrderSelector")


class OrderSelector(_1809.OrderForTE):
    """OrderSelector

    This is a mastapy class.
    """

    TYPE = _ORDER_SELECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OrderSelector")

    class _Cast_OrderSelector:
        """Special nested class for casting OrderSelector to subclasses."""

        def __init__(
            self: "OrderSelector._Cast_OrderSelector", parent: "OrderSelector"
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "OrderSelector._Cast_OrderSelector",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def order_selector(
            self: "OrderSelector._Cast_OrderSelector",
        ) -> "OrderSelector":
            return self._parent

        def __getattr__(self: "OrderSelector._Cast_OrderSelector", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OrderSelector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OrderSelector._Cast_OrderSelector":
        return self._Cast_OrderSelector(self)
