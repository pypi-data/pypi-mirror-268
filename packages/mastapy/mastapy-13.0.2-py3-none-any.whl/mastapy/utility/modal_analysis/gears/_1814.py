"""UserDefinedOrderForTE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.modal_analysis.gears import _1811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_DEFINED_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "UserDefinedOrderForTE"
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis.gears import _1809


__docformat__ = "restructuredtext en"
__all__ = ("UserDefinedOrderForTE",)


Self = TypeVar("Self", bound="UserDefinedOrderForTE")


class UserDefinedOrderForTE(_1811.OrderWithRadius):
    """UserDefinedOrderForTE

    This is a mastapy class.
    """

    TYPE = _USER_DEFINED_ORDER_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UserDefinedOrderForTE")

    class _Cast_UserDefinedOrderForTE:
        """Special nested class for casting UserDefinedOrderForTE to subclasses."""

        def __init__(
            self: "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE",
            parent: "UserDefinedOrderForTE",
        ):
            self._parent = parent

        @property
        def order_with_radius(
            self: "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE",
        ) -> "_1811.OrderWithRadius":
            return self._parent._cast(_1811.OrderWithRadius)

        @property
        def order_for_te(
            self: "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE",
        ) -> "_1809.OrderForTE":
            from mastapy.utility.modal_analysis.gears import _1809

            return self._parent._cast(_1809.OrderForTE)

        @property
        def user_defined_order_for_te(
            self: "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE",
        ) -> "UserDefinedOrderForTE":
            return self._parent

        def __getattr__(
            self: "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UserDefinedOrderForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "UserDefinedOrderForTE._Cast_UserDefinedOrderForTE":
        return self._Cast_UserDefinedOrderForTE(self)
