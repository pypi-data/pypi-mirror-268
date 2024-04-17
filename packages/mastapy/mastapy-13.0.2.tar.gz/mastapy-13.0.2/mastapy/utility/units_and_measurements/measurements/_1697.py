"""Power"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Power"
)


__docformat__ = "restructuredtext en"
__all__ = ("Power",)


Self = TypeVar("Self", bound="Power")


class Power(_1612.MeasurementBase):
    """Power

    This is a mastapy class.
    """

    TYPE = _POWER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Power")

    class _Cast_Power:
        """Special nested class for casting Power to subclasses."""

        def __init__(self: "Power._Cast_Power", parent: "Power"):
            self._parent = parent

        @property
        def measurement_base(self: "Power._Cast_Power") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power(self: "Power._Cast_Power") -> "Power":
            return self._parent

        def __getattr__(self: "Power._Cast_Power", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Power.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Power._Cast_Power":
        return self._Cast_Power(self)
