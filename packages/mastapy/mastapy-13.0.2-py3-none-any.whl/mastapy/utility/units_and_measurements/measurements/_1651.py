"""ForcePerUnitPressure"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_PRESSURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ForcePerUnitPressure"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForcePerUnitPressure",)


Self = TypeVar("Self", bound="ForcePerUnitPressure")


class ForcePerUnitPressure(_1612.MeasurementBase):
    """ForcePerUnitPressure

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_PRESSURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForcePerUnitPressure")

    class _Cast_ForcePerUnitPressure:
        """Special nested class for casting ForcePerUnitPressure to subclasses."""

        def __init__(
            self: "ForcePerUnitPressure._Cast_ForcePerUnitPressure",
            parent: "ForcePerUnitPressure",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ForcePerUnitPressure._Cast_ForcePerUnitPressure",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def force_per_unit_pressure(
            self: "ForcePerUnitPressure._Cast_ForcePerUnitPressure",
        ) -> "ForcePerUnitPressure":
            return self._parent

        def __getattr__(
            self: "ForcePerUnitPressure._Cast_ForcePerUnitPressure", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForcePerUnitPressure.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ForcePerUnitPressure._Cast_ForcePerUnitPressure":
        return self._Cast_ForcePerUnitPressure(self)
