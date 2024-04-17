"""HeatConductivity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_CONDUCTIVITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "HeatConductivity"
)


__docformat__ = "restructuredtext en"
__all__ = ("HeatConductivity",)


Self = TypeVar("Self", bound="HeatConductivity")


class HeatConductivity(_1612.MeasurementBase):
    """HeatConductivity

    This is a mastapy class.
    """

    TYPE = _HEAT_CONDUCTIVITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HeatConductivity")

    class _Cast_HeatConductivity:
        """Special nested class for casting HeatConductivity to subclasses."""

        def __init__(
            self: "HeatConductivity._Cast_HeatConductivity", parent: "HeatConductivity"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "HeatConductivity._Cast_HeatConductivity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def heat_conductivity(
            self: "HeatConductivity._Cast_HeatConductivity",
        ) -> "HeatConductivity":
            return self._parent

        def __getattr__(self: "HeatConductivity._Cast_HeatConductivity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HeatConductivity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HeatConductivity._Cast_HeatConductivity":
        return self._Cast_HeatConductivity(self)
