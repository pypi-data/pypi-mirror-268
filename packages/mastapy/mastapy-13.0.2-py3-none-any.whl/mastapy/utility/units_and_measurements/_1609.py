"""DegreesMinutesSeconds"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREES_MINUTES_SECONDS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "DegreesMinutesSeconds"
)


__docformat__ = "restructuredtext en"
__all__ = ("DegreesMinutesSeconds",)


Self = TypeVar("Self", bound="DegreesMinutesSeconds")


class DegreesMinutesSeconds(_1617.Unit):
    """DegreesMinutesSeconds

    This is a mastapy class.
    """

    TYPE = _DEGREES_MINUTES_SECONDS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DegreesMinutesSeconds")

    class _Cast_DegreesMinutesSeconds:
        """Special nested class for casting DegreesMinutesSeconds to subclasses."""

        def __init__(
            self: "DegreesMinutesSeconds._Cast_DegreesMinutesSeconds",
            parent: "DegreesMinutesSeconds",
        ):
            self._parent = parent

        @property
        def unit(
            self: "DegreesMinutesSeconds._Cast_DegreesMinutesSeconds",
        ) -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def degrees_minutes_seconds(
            self: "DegreesMinutesSeconds._Cast_DegreesMinutesSeconds",
        ) -> "DegreesMinutesSeconds":
            return self._parent

        def __getattr__(
            self: "DegreesMinutesSeconds._Cast_DegreesMinutesSeconds", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DegreesMinutesSeconds.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DegreesMinutesSeconds._Cast_DegreesMinutesSeconds":
        return self._Cast_DegreesMinutesSeconds(self)
