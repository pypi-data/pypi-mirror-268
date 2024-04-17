"""HeatTransferResistance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER_RESISTANCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "HeatTransferResistance"
)


__docformat__ = "restructuredtext en"
__all__ = ("HeatTransferResistance",)


Self = TypeVar("Self", bound="HeatTransferResistance")


class HeatTransferResistance(_1612.MeasurementBase):
    """HeatTransferResistance

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER_RESISTANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HeatTransferResistance")

    class _Cast_HeatTransferResistance:
        """Special nested class for casting HeatTransferResistance to subclasses."""

        def __init__(
            self: "HeatTransferResistance._Cast_HeatTransferResistance",
            parent: "HeatTransferResistance",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "HeatTransferResistance._Cast_HeatTransferResistance",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def heat_transfer_resistance(
            self: "HeatTransferResistance._Cast_HeatTransferResistance",
        ) -> "HeatTransferResistance":
            return self._parent

        def __getattr__(
            self: "HeatTransferResistance._Cast_HeatTransferResistance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HeatTransferResistance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HeatTransferResistance._Cast_HeatTransferResistance":
        return self._Cast_HeatTransferResistance(self)
