"""EnergyPerUnitAreaSmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY_PER_UNIT_AREA_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "EnergyPerUnitAreaSmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnergyPerUnitAreaSmall",)


Self = TypeVar("Self", bound="EnergyPerUnitAreaSmall")


class EnergyPerUnitAreaSmall(_1612.MeasurementBase):
    """EnergyPerUnitAreaSmall

    This is a mastapy class.
    """

    TYPE = _ENERGY_PER_UNIT_AREA_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnergyPerUnitAreaSmall")

    class _Cast_EnergyPerUnitAreaSmall:
        """Special nested class for casting EnergyPerUnitAreaSmall to subclasses."""

        def __init__(
            self: "EnergyPerUnitAreaSmall._Cast_EnergyPerUnitAreaSmall",
            parent: "EnergyPerUnitAreaSmall",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "EnergyPerUnitAreaSmall._Cast_EnergyPerUnitAreaSmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def energy_per_unit_area_small(
            self: "EnergyPerUnitAreaSmall._Cast_EnergyPerUnitAreaSmall",
        ) -> "EnergyPerUnitAreaSmall":
            return self._parent

        def __getattr__(
            self: "EnergyPerUnitAreaSmall._Cast_EnergyPerUnitAreaSmall", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnergyPerUnitAreaSmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "EnergyPerUnitAreaSmall._Cast_EnergyPerUnitAreaSmall":
        return self._Cast_EnergyPerUnitAreaSmall(self)
