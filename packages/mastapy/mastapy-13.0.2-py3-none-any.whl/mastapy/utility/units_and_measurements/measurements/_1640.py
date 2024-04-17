"""ElectricalResistance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTANCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ElectricalResistance"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricalResistance",)


Self = TypeVar("Self", bound="ElectricalResistance")


class ElectricalResistance(_1612.MeasurementBase):
    """ElectricalResistance

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricalResistance")

    class _Cast_ElectricalResistance:
        """Special nested class for casting ElectricalResistance to subclasses."""

        def __init__(
            self: "ElectricalResistance._Cast_ElectricalResistance",
            parent: "ElectricalResistance",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ElectricalResistance._Cast_ElectricalResistance",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def electrical_resistance(
            self: "ElectricalResistance._Cast_ElectricalResistance",
        ) -> "ElectricalResistance":
            return self._parent

        def __getattr__(
            self: "ElectricalResistance._Cast_ElectricalResistance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricalResistance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElectricalResistance._Cast_ElectricalResistance":
        return self._Cast_ElectricalResistance(self)
