"""FuelEfficiencyVehicle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FUEL_EFFICIENCY_VEHICLE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "FuelEfficiencyVehicle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FuelEfficiencyVehicle",)


Self = TypeVar("Self", bound="FuelEfficiencyVehicle")


class FuelEfficiencyVehicle(_1612.MeasurementBase):
    """FuelEfficiencyVehicle

    This is a mastapy class.
    """

    TYPE = _FUEL_EFFICIENCY_VEHICLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FuelEfficiencyVehicle")

    class _Cast_FuelEfficiencyVehicle:
        """Special nested class for casting FuelEfficiencyVehicle to subclasses."""

        def __init__(
            self: "FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle",
            parent: "FuelEfficiencyVehicle",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def fuel_efficiency_vehicle(
            self: "FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle",
        ) -> "FuelEfficiencyVehicle":
            return self._parent

        def __getattr__(
            self: "FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FuelEfficiencyVehicle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle":
        return self._Cast_FuelEfficiencyVehicle(self)
