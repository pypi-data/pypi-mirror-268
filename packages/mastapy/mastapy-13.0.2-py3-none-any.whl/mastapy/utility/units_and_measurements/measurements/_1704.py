"""PowerSmallPerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PowerSmallPerUnitTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerSmallPerUnitTime",)


Self = TypeVar("Self", bound="PowerSmallPerUnitTime")


class PowerSmallPerUnitTime(_1612.MeasurementBase):
    """PowerSmallPerUnitTime

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerSmallPerUnitTime")

    class _Cast_PowerSmallPerUnitTime:
        """Special nested class for casting PowerSmallPerUnitTime to subclasses."""

        def __init__(
            self: "PowerSmallPerUnitTime._Cast_PowerSmallPerUnitTime",
            parent: "PowerSmallPerUnitTime",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerSmallPerUnitTime._Cast_PowerSmallPerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_small_per_unit_time(
            self: "PowerSmallPerUnitTime._Cast_PowerSmallPerUnitTime",
        ) -> "PowerSmallPerUnitTime":
            return self._parent

        def __getattr__(
            self: "PowerSmallPerUnitTime._Cast_PowerSmallPerUnitTime", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerSmallPerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PowerSmallPerUnitTime._Cast_PowerSmallPerUnitTime":
        return self._Cast_PowerSmallPerUnitTime(self)
