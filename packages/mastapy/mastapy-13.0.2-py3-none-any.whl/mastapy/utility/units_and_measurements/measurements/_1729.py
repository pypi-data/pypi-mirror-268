"""Time"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Time"
)


__docformat__ = "restructuredtext en"
__all__ = ("Time",)


Self = TypeVar("Self", bound="Time")


class Time(_1612.MeasurementBase):
    """Time

    This is a mastapy class.
    """

    TYPE = _TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Time")

    class _Cast_Time:
        """Special nested class for casting Time to subclasses."""

        def __init__(self: "Time._Cast_Time", parent: "Time"):
            self._parent = parent

        @property
        def measurement_base(self: "Time._Cast_Time") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def time(self: "Time._Cast_Time") -> "Time":
            return self._parent

        def __getattr__(self: "Time._Cast_Time", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Time.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Time._Cast_Time":
        return self._Cast_Time(self)
