"""TimeUnit"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_UNIT = python_net_import("SMT.MastaAPI.Utility.UnitsAndMeasurements", "TimeUnit")


__docformat__ = "restructuredtext en"
__all__ = ("TimeUnit",)


Self = TypeVar("Self", bound="TimeUnit")


class TimeUnit(_1617.Unit):
    """TimeUnit

    This is a mastapy class.
    """

    TYPE = _TIME_UNIT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeUnit")

    class _Cast_TimeUnit:
        """Special nested class for casting TimeUnit to subclasses."""

        def __init__(self: "TimeUnit._Cast_TimeUnit", parent: "TimeUnit"):
            self._parent = parent

        @property
        def unit(self: "TimeUnit._Cast_TimeUnit") -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def time_unit(self: "TimeUnit._Cast_TimeUnit") -> "TimeUnit":
            return self._parent

        def __getattr__(self: "TimeUnit._Cast_TimeUnit", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeUnit.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TimeUnit._Cast_TimeUnit":
        return self._Cast_TimeUnit(self)
