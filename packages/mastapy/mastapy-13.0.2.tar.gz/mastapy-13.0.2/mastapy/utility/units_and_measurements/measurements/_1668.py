"""InverseShortTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_SHORT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "InverseShortTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("InverseShortTime",)


Self = TypeVar("Self", bound="InverseShortTime")


class InverseShortTime(_1612.MeasurementBase):
    """InverseShortTime

    This is a mastapy class.
    """

    TYPE = _INVERSE_SHORT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InverseShortTime")

    class _Cast_InverseShortTime:
        """Special nested class for casting InverseShortTime to subclasses."""

        def __init__(
            self: "InverseShortTime._Cast_InverseShortTime", parent: "InverseShortTime"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "InverseShortTime._Cast_InverseShortTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def inverse_short_time(
            self: "InverseShortTime._Cast_InverseShortTime",
        ) -> "InverseShortTime":
            return self._parent

        def __getattr__(self: "InverseShortTime._Cast_InverseShortTime", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InverseShortTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InverseShortTime._Cast_InverseShortTime":
        return self._Cast_InverseShortTime(self)
