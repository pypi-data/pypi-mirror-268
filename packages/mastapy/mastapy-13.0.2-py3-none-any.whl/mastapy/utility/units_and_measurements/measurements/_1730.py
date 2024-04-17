"""TimeShort"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SHORT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TimeShort"
)


__docformat__ = "restructuredtext en"
__all__ = ("TimeShort",)


Self = TypeVar("Self", bound="TimeShort")


class TimeShort(_1612.MeasurementBase):
    """TimeShort

    This is a mastapy class.
    """

    TYPE = _TIME_SHORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeShort")

    class _Cast_TimeShort:
        """Special nested class for casting TimeShort to subclasses."""

        def __init__(self: "TimeShort._Cast_TimeShort", parent: "TimeShort"):
            self._parent = parent

        @property
        def measurement_base(
            self: "TimeShort._Cast_TimeShort",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def time_short(self: "TimeShort._Cast_TimeShort") -> "TimeShort":
            return self._parent

        def __getattr__(self: "TimeShort._Cast_TimeShort", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeShort.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TimeShort._Cast_TimeShort":
        return self._Cast_TimeShort(self)
