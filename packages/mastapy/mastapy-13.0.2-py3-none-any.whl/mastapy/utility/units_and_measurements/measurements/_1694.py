"""MomentPerUnitPressure"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_PER_UNIT_PRESSURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MomentPerUnitPressure"
)


__docformat__ = "restructuredtext en"
__all__ = ("MomentPerUnitPressure",)


Self = TypeVar("Self", bound="MomentPerUnitPressure")


class MomentPerUnitPressure(_1612.MeasurementBase):
    """MomentPerUnitPressure

    This is a mastapy class.
    """

    TYPE = _MOMENT_PER_UNIT_PRESSURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MomentPerUnitPressure")

    class _Cast_MomentPerUnitPressure:
        """Special nested class for casting MomentPerUnitPressure to subclasses."""

        def __init__(
            self: "MomentPerUnitPressure._Cast_MomentPerUnitPressure",
            parent: "MomentPerUnitPressure",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MomentPerUnitPressure._Cast_MomentPerUnitPressure",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def moment_per_unit_pressure(
            self: "MomentPerUnitPressure._Cast_MomentPerUnitPressure",
        ) -> "MomentPerUnitPressure":
            return self._parent

        def __getattr__(
            self: "MomentPerUnitPressure._Cast_MomentPerUnitPressure", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MomentPerUnitPressure.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MomentPerUnitPressure._Cast_MomentPerUnitPressure":
        return self._Cast_MomentPerUnitPressure(self)
