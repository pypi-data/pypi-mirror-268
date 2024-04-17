"""Voltage"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLTAGE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Voltage"
)


__docformat__ = "restructuredtext en"
__all__ = ("Voltage",)


Self = TypeVar("Self", bound="Voltage")


class Voltage(_1612.MeasurementBase):
    """Voltage

    This is a mastapy class.
    """

    TYPE = _VOLTAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Voltage")

    class _Cast_Voltage:
        """Special nested class for casting Voltage to subclasses."""

        def __init__(self: "Voltage._Cast_Voltage", parent: "Voltage"):
            self._parent = parent

        @property
        def measurement_base(self: "Voltage._Cast_Voltage") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def voltage(self: "Voltage._Cast_Voltage") -> "Voltage":
            return self._parent

        def __getattr__(self: "Voltage._Cast_Voltage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Voltage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Voltage._Cast_Voltage":
        return self._Cast_Voltage(self)
