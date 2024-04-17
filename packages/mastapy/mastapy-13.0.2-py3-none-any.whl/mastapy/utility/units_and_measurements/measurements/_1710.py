"""Price"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRICE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Price"
)


__docformat__ = "restructuredtext en"
__all__ = ("Price",)


Self = TypeVar("Self", bound="Price")


class Price(_1612.MeasurementBase):
    """Price

    This is a mastapy class.
    """

    TYPE = _PRICE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Price")

    class _Cast_Price:
        """Special nested class for casting Price to subclasses."""

        def __init__(self: "Price._Cast_Price", parent: "Price"):
            self._parent = parent

        @property
        def measurement_base(self: "Price._Cast_Price") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def price(self: "Price._Cast_Price") -> "Price":
            return self._parent

        def __getattr__(self: "Price._Cast_Price", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Price.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Price._Cast_Price":
        return self._Cast_Price(self)
