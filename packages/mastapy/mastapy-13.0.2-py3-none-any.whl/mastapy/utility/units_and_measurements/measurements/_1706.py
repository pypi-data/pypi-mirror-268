"""Pressure"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.units_and_measurements.measurements import _1721
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Pressure"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("Pressure",)


Self = TypeVar("Self", bound="Pressure")


class Pressure(_1721.Stress):
    """Pressure

    This is a mastapy class.
    """

    TYPE = _PRESSURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Pressure")

    class _Cast_Pressure:
        """Special nested class for casting Pressure to subclasses."""

        def __init__(self: "Pressure._Cast_Pressure", parent: "Pressure"):
            self._parent = parent

        @property
        def stress(self: "Pressure._Cast_Pressure") -> "_1721.Stress":
            return self._parent._cast(_1721.Stress)

        @property
        def measurement_base(
            self: "Pressure._Cast_Pressure",
        ) -> "_1612.MeasurementBase":
            from mastapy.utility.units_and_measurements import _1612

            return self._parent._cast(_1612.MeasurementBase)

        @property
        def pressure(self: "Pressure._Cast_Pressure") -> "Pressure":
            return self._parent

        def __getattr__(self: "Pressure._Cast_Pressure", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Pressure.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Pressure._Cast_Pressure":
        return self._Cast_Pressure(self)
