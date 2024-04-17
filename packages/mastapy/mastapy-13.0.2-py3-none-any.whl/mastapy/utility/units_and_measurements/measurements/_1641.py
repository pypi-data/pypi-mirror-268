"""ElectricalResistivity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTIVITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ElectricalResistivity"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricalResistivity",)


Self = TypeVar("Self", bound="ElectricalResistivity")


class ElectricalResistivity(_1612.MeasurementBase):
    """ElectricalResistivity

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTIVITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricalResistivity")

    class _Cast_ElectricalResistivity:
        """Special nested class for casting ElectricalResistivity to subclasses."""

        def __init__(
            self: "ElectricalResistivity._Cast_ElectricalResistivity",
            parent: "ElectricalResistivity",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ElectricalResistivity._Cast_ElectricalResistivity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def electrical_resistivity(
            self: "ElectricalResistivity._Cast_ElectricalResistivity",
        ) -> "ElectricalResistivity":
            return self._parent

        def __getattr__(
            self: "ElectricalResistivity._Cast_ElectricalResistivity", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricalResistivity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElectricalResistivity._Cast_ElectricalResistivity":
        return self._Cast_ElectricalResistivity(self)
