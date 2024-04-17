"""LabelOnlyOrder"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LABEL_ONLY_ORDER = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "LabelOnlyOrder"
)


__docformat__ = "restructuredtext en"
__all__ = ("LabelOnlyOrder",)


Self = TypeVar("Self", bound="LabelOnlyOrder")


class LabelOnlyOrder(_1809.OrderForTE):
    """LabelOnlyOrder

    This is a mastapy class.
    """

    TYPE = _LABEL_ONLY_ORDER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LabelOnlyOrder")

    class _Cast_LabelOnlyOrder:
        """Special nested class for casting LabelOnlyOrder to subclasses."""

        def __init__(
            self: "LabelOnlyOrder._Cast_LabelOnlyOrder", parent: "LabelOnlyOrder"
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "LabelOnlyOrder._Cast_LabelOnlyOrder",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def label_only_order(
            self: "LabelOnlyOrder._Cast_LabelOnlyOrder",
        ) -> "LabelOnlyOrder":
            return self._parent

        def __getattr__(self: "LabelOnlyOrder._Cast_LabelOnlyOrder", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LabelOnlyOrder.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LabelOnlyOrder._Cast_LabelOnlyOrder":
        return self._Cast_LabelOnlyOrder(self)
