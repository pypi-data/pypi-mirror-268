"""PressurePerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PressurePerUnitTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("PressurePerUnitTime",)


Self = TypeVar("Self", bound="PressurePerUnitTime")


class PressurePerUnitTime(_1612.MeasurementBase):
    """PressurePerUnitTime

    This is a mastapy class.
    """

    TYPE = _PRESSURE_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PressurePerUnitTime")

    class _Cast_PressurePerUnitTime:
        """Special nested class for casting PressurePerUnitTime to subclasses."""

        def __init__(
            self: "PressurePerUnitTime._Cast_PressurePerUnitTime",
            parent: "PressurePerUnitTime",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PressurePerUnitTime._Cast_PressurePerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def pressure_per_unit_time(
            self: "PressurePerUnitTime._Cast_PressurePerUnitTime",
        ) -> "PressurePerUnitTime":
            return self._parent

        def __getattr__(
            self: "PressurePerUnitTime._Cast_PressurePerUnitTime", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PressurePerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PressurePerUnitTime._Cast_PressurePerUnitTime":
        return self._Cast_PressurePerUnitTime(self)
