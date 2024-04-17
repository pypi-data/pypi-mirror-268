"""TemperatureDifference"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURE_DIFFERENCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TemperatureDifference"
)


__docformat__ = "restructuredtext en"
__all__ = ("TemperatureDifference",)


Self = TypeVar("Self", bound="TemperatureDifference")


class TemperatureDifference(_1612.MeasurementBase):
    """TemperatureDifference

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE_DIFFERENCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TemperatureDifference")

    class _Cast_TemperatureDifference:
        """Special nested class for casting TemperatureDifference to subclasses."""

        def __init__(
            self: "TemperatureDifference._Cast_TemperatureDifference",
            parent: "TemperatureDifference",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TemperatureDifference._Cast_TemperatureDifference",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def temperature_difference(
            self: "TemperatureDifference._Cast_TemperatureDifference",
        ) -> "TemperatureDifference":
            return self._parent

        def __getattr__(
            self: "TemperatureDifference._Cast_TemperatureDifference", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TemperatureDifference.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TemperatureDifference._Cast_TemperatureDifference":
        return self._Cast_TemperatureDifference(self)
