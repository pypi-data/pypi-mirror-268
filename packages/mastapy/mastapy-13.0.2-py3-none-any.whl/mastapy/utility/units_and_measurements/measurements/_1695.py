"""Number"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NUMBER = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Number"
)


__docformat__ = "restructuredtext en"
__all__ = ("Number",)


Self = TypeVar("Self", bound="Number")


class Number(_1612.MeasurementBase):
    """Number

    This is a mastapy class.
    """

    TYPE = _NUMBER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Number")

    class _Cast_Number:
        """Special nested class for casting Number to subclasses."""

        def __init__(self: "Number._Cast_Number", parent: "Number"):
            self._parent = parent

        @property
        def measurement_base(self: "Number._Cast_Number") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def number(self: "Number._Cast_Number") -> "Number":
            return self._parent

        def __getattr__(self: "Number._Cast_Number", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Number.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Number._Cast_Number":
        return self._Cast_Number(self)
