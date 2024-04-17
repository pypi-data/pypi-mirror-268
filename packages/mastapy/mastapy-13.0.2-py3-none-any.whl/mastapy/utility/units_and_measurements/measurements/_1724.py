"""TemperaturePerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURE_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TemperaturePerUnitTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("TemperaturePerUnitTime",)


Self = TypeVar("Self", bound="TemperaturePerUnitTime")


class TemperaturePerUnitTime(_1612.MeasurementBase):
    """TemperaturePerUnitTime

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TemperaturePerUnitTime")

    class _Cast_TemperaturePerUnitTime:
        """Special nested class for casting TemperaturePerUnitTime to subclasses."""

        def __init__(
            self: "TemperaturePerUnitTime._Cast_TemperaturePerUnitTime",
            parent: "TemperaturePerUnitTime",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TemperaturePerUnitTime._Cast_TemperaturePerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def temperature_per_unit_time(
            self: "TemperaturePerUnitTime._Cast_TemperaturePerUnitTime",
        ) -> "TemperaturePerUnitTime":
            return self._parent

        def __getattr__(
            self: "TemperaturePerUnitTime._Cast_TemperaturePerUnitTime", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TemperaturePerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TemperaturePerUnitTime._Cast_TemperaturePerUnitTime":
        return self._Cast_TemperaturePerUnitTime(self)
