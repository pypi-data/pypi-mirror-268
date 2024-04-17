"""Frequency"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Frequency"
)


__docformat__ = "restructuredtext en"
__all__ = ("Frequency",)


Self = TypeVar("Self", bound="Frequency")


class Frequency(_1612.MeasurementBase):
    """Frequency

    This is a mastapy class.
    """

    TYPE = _FREQUENCY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Frequency")

    class _Cast_Frequency:
        """Special nested class for casting Frequency to subclasses."""

        def __init__(self: "Frequency._Cast_Frequency", parent: "Frequency"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Frequency._Cast_Frequency",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def frequency(self: "Frequency._Cast_Frequency") -> "Frequency":
            return self._parent

        def __getattr__(self: "Frequency._Cast_Frequency", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Frequency.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Frequency._Cast_Frequency":
        return self._Cast_Frequency(self)
