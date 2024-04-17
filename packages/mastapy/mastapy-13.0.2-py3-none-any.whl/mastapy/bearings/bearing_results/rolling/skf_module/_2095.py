"""GreaseQuantity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GREASE_QUANTITY = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "GreaseQuantity"
)


__docformat__ = "restructuredtext en"
__all__ = ("GreaseQuantity",)


Self = TypeVar("Self", bound="GreaseQuantity")


class GreaseQuantity(_2103.SKFCalculationResult):
    """GreaseQuantity

    This is a mastapy class.
    """

    TYPE = _GREASE_QUANTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GreaseQuantity")

    class _Cast_GreaseQuantity:
        """Special nested class for casting GreaseQuantity to subclasses."""

        def __init__(
            self: "GreaseQuantity._Cast_GreaseQuantity", parent: "GreaseQuantity"
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "GreaseQuantity._Cast_GreaseQuantity",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def grease_quantity(
            self: "GreaseQuantity._Cast_GreaseQuantity",
        ) -> "GreaseQuantity":
            return self._parent

        def __getattr__(self: "GreaseQuantity._Cast_GreaseQuantity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GreaseQuantity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ring

        if temp is None:
            return 0.0

        return temp

    @property
    def side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Side

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "GreaseQuantity._Cast_GreaseQuantity":
        return self._Cast_GreaseQuantity(self)
