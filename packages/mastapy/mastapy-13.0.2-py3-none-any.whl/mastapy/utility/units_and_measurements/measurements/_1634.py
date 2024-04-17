"""Cycles"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLES = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Cycles"
)


__docformat__ = "restructuredtext en"
__all__ = ("Cycles",)


Self = TypeVar("Self", bound="Cycles")


class Cycles(_1612.MeasurementBase):
    """Cycles

    This is a mastapy class.
    """

    TYPE = _CYCLES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Cycles")

    class _Cast_Cycles:
        """Special nested class for casting Cycles to subclasses."""

        def __init__(self: "Cycles._Cast_Cycles", parent: "Cycles"):
            self._parent = parent

        @property
        def measurement_base(self: "Cycles._Cast_Cycles") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def cycles(self: "Cycles._Cast_Cycles") -> "Cycles":
            return self._parent

        def __getattr__(self: "Cycles._Cast_Cycles", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Cycles.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Cycles._Cast_Cycles":
        return self._Cast_Cycles(self)
