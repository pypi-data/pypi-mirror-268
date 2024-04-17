"""Temperature"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Temperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("Temperature",)


Self = TypeVar("Self", bound="Temperature")


class Temperature(_1612.MeasurementBase):
    """Temperature

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Temperature")

    class _Cast_Temperature:
        """Special nested class for casting Temperature to subclasses."""

        def __init__(self: "Temperature._Cast_Temperature", parent: "Temperature"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Temperature._Cast_Temperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def temperature(self: "Temperature._Cast_Temperature") -> "Temperature":
            return self._parent

        def __getattr__(self: "Temperature._Cast_Temperature", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Temperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Temperature._Cast_Temperature":
        return self._Cast_Temperature(self)
