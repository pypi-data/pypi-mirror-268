"""TimeVeryShort"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_VERY_SHORT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TimeVeryShort"
)


__docformat__ = "restructuredtext en"
__all__ = ("TimeVeryShort",)


Self = TypeVar("Self", bound="TimeVeryShort")


class TimeVeryShort(_1612.MeasurementBase):
    """TimeVeryShort

    This is a mastapy class.
    """

    TYPE = _TIME_VERY_SHORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeVeryShort")

    class _Cast_TimeVeryShort:
        """Special nested class for casting TimeVeryShort to subclasses."""

        def __init__(
            self: "TimeVeryShort._Cast_TimeVeryShort", parent: "TimeVeryShort"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TimeVeryShort._Cast_TimeVeryShort",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def time_very_short(
            self: "TimeVeryShort._Cast_TimeVeryShort",
        ) -> "TimeVeryShort":
            return self._parent

        def __getattr__(self: "TimeVeryShort._Cast_TimeVeryShort", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeVeryShort.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TimeVeryShort._Cast_TimeVeryShort":
        return self._Cast_TimeVeryShort(self)
