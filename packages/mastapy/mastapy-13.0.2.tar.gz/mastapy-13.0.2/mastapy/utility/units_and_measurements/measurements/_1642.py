"""ElectricCurrent"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_CURRENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ElectricCurrent"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricCurrent",)


Self = TypeVar("Self", bound="ElectricCurrent")


class ElectricCurrent(_1612.MeasurementBase):
    """ElectricCurrent

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_CURRENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricCurrent")

    class _Cast_ElectricCurrent:
        """Special nested class for casting ElectricCurrent to subclasses."""

        def __init__(
            self: "ElectricCurrent._Cast_ElectricCurrent", parent: "ElectricCurrent"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ElectricCurrent._Cast_ElectricCurrent",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def electric_current(
            self: "ElectricCurrent._Cast_ElectricCurrent",
        ) -> "ElectricCurrent":
            return self._parent

        def __getattr__(self: "ElectricCurrent._Cast_ElectricCurrent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricCurrent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElectricCurrent._Cast_ElectricCurrent":
        return self._Cast_ElectricCurrent(self)
