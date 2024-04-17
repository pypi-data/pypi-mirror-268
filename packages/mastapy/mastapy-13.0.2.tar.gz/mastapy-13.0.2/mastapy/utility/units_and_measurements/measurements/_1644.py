"""EnergyPerUnitArea"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY_PER_UNIT_AREA = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "EnergyPerUnitArea"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnergyPerUnitArea",)


Self = TypeVar("Self", bound="EnergyPerUnitArea")


class EnergyPerUnitArea(_1612.MeasurementBase):
    """EnergyPerUnitArea

    This is a mastapy class.
    """

    TYPE = _ENERGY_PER_UNIT_AREA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnergyPerUnitArea")

    class _Cast_EnergyPerUnitArea:
        """Special nested class for casting EnergyPerUnitArea to subclasses."""

        def __init__(
            self: "EnergyPerUnitArea._Cast_EnergyPerUnitArea",
            parent: "EnergyPerUnitArea",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "EnergyPerUnitArea._Cast_EnergyPerUnitArea",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def energy_per_unit_area(
            self: "EnergyPerUnitArea._Cast_EnergyPerUnitArea",
        ) -> "EnergyPerUnitArea":
            return self._parent

        def __getattr__(self: "EnergyPerUnitArea._Cast_EnergyPerUnitArea", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnergyPerUnitArea.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "EnergyPerUnitArea._Cast_EnergyPerUnitArea":
        return self._Cast_EnergyPerUnitArea(self)
