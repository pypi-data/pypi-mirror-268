"""PowerPerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PowerPerUnitTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerPerUnitTime",)


Self = TypeVar("Self", bound="PowerPerUnitTime")


class PowerPerUnitTime(_1612.MeasurementBase):
    """PowerPerUnitTime

    This is a mastapy class.
    """

    TYPE = _POWER_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerPerUnitTime")

    class _Cast_PowerPerUnitTime:
        """Special nested class for casting PowerPerUnitTime to subclasses."""

        def __init__(
            self: "PowerPerUnitTime._Cast_PowerPerUnitTime", parent: "PowerPerUnitTime"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerPerUnitTime._Cast_PowerPerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_per_unit_time(
            self: "PowerPerUnitTime._Cast_PowerPerUnitTime",
        ) -> "PowerPerUnitTime":
            return self._parent

        def __getattr__(self: "PowerPerUnitTime._Cast_PowerPerUnitTime", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerPerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PowerPerUnitTime._Cast_PowerPerUnitTime":
        return self._Cast_PowerPerUnitTime(self)
