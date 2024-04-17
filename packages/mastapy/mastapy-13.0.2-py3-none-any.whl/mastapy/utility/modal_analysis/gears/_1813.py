"""ShaftOrderForTE"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "ShaftOrderForTE"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftOrderForTE",)


Self = TypeVar("Self", bound="ShaftOrderForTE")


class ShaftOrderForTE(_1809.OrderForTE):
    """ShaftOrderForTE

    This is a mastapy class.
    """

    TYPE = _SHAFT_ORDER_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftOrderForTE")

    class _Cast_ShaftOrderForTE:
        """Special nested class for casting ShaftOrderForTE to subclasses."""

        def __init__(
            self: "ShaftOrderForTE._Cast_ShaftOrderForTE", parent: "ShaftOrderForTE"
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "ShaftOrderForTE._Cast_ShaftOrderForTE",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def shaft_order_for_te(
            self: "ShaftOrderForTE._Cast_ShaftOrderForTE",
        ) -> "ShaftOrderForTE":
            return self._parent

        def __getattr__(self: "ShaftOrderForTE._Cast_ShaftOrderForTE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftOrderForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftOrderForTE._Cast_ShaftOrderForTE":
        return self._Cast_ShaftOrderForTE(self)
