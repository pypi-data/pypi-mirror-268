"""EnergySmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "EnergySmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnergySmall",)


Self = TypeVar("Self", bound="EnergySmall")


class EnergySmall(_1612.MeasurementBase):
    """EnergySmall

    This is a mastapy class.
    """

    TYPE = _ENERGY_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnergySmall")

    class _Cast_EnergySmall:
        """Special nested class for casting EnergySmall to subclasses."""

        def __init__(self: "EnergySmall._Cast_EnergySmall", parent: "EnergySmall"):
            self._parent = parent

        @property
        def measurement_base(
            self: "EnergySmall._Cast_EnergySmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def energy_small(self: "EnergySmall._Cast_EnergySmall") -> "EnergySmall":
            return self._parent

        def __getattr__(self: "EnergySmall._Cast_EnergySmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnergySmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "EnergySmall._Cast_EnergySmall":
        return self._Cast_EnergySmall(self)
