"""RollingBearingOrder"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_ORDER = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "RollingBearingOrder"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingOrder",)


Self = TypeVar("Self", bound="RollingBearingOrder")


class RollingBearingOrder(_1809.OrderForTE):
    """RollingBearingOrder

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_ORDER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingOrder")

    class _Cast_RollingBearingOrder:
        """Special nested class for casting RollingBearingOrder to subclasses."""

        def __init__(
            self: "RollingBearingOrder._Cast_RollingBearingOrder",
            parent: "RollingBearingOrder",
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "RollingBearingOrder._Cast_RollingBearingOrder",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def rolling_bearing_order(
            self: "RollingBearingOrder._Cast_RollingBearingOrder",
        ) -> "RollingBearingOrder":
            return self._parent

        def __getattr__(
            self: "RollingBearingOrder._Cast_RollingBearingOrder", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearingOrder.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RollingBearingOrder._Cast_RollingBearingOrder":
        return self._Cast_RollingBearingOrder(self)
