"""OrderWithRadius"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_WITH_RADIUS = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "OrderWithRadius"
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis.gears import _1805, _1814


__docformat__ = "restructuredtext en"
__all__ = ("OrderWithRadius",)


Self = TypeVar("Self", bound="OrderWithRadius")


class OrderWithRadius(_1809.OrderForTE):
    """OrderWithRadius

    This is a mastapy class.
    """

    TYPE = _ORDER_WITH_RADIUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OrderWithRadius")

    class _Cast_OrderWithRadius:
        """Special nested class for casting OrderWithRadius to subclasses."""

        def __init__(
            self: "OrderWithRadius._Cast_OrderWithRadius", parent: "OrderWithRadius"
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "OrderWithRadius._Cast_OrderWithRadius",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def gear_order_for_te(
            self: "OrderWithRadius._Cast_OrderWithRadius",
        ) -> "_1805.GearOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1805

            return self._parent._cast(_1805.GearOrderForTE)

        @property
        def user_defined_order_for_te(
            self: "OrderWithRadius._Cast_OrderWithRadius",
        ) -> "_1814.UserDefinedOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1814

            return self._parent._cast(_1814.UserDefinedOrderForTE)

        @property
        def order_with_radius(
            self: "OrderWithRadius._Cast_OrderWithRadius",
        ) -> "OrderWithRadius":
            return self._parent

        def __getattr__(self: "OrderWithRadius._Cast_OrderWithRadius", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OrderWithRadius.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "OrderWithRadius._Cast_OrderWithRadius":
        return self._Cast_OrderWithRadius(self)
