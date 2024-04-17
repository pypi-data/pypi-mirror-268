"""TorquePerUnitTemperature"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_UNIT_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "TorquePerUnitTemperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorquePerUnitTemperature",)


Self = TypeVar("Self", bound="TorquePerUnitTemperature")


class TorquePerUnitTemperature(_1612.MeasurementBase):
    """TorquePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_UNIT_TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorquePerUnitTemperature")

    class _Cast_TorquePerUnitTemperature:
        """Special nested class for casting TorquePerUnitTemperature to subclasses."""

        def __init__(
            self: "TorquePerUnitTemperature._Cast_TorquePerUnitTemperature",
            parent: "TorquePerUnitTemperature",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "TorquePerUnitTemperature._Cast_TorquePerUnitTemperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def torque_per_unit_temperature(
            self: "TorquePerUnitTemperature._Cast_TorquePerUnitTemperature",
        ) -> "TorquePerUnitTemperature":
            return self._parent

        def __getattr__(
            self: "TorquePerUnitTemperature._Cast_TorquePerUnitTemperature", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorquePerUnitTemperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorquePerUnitTemperature._Cast_TorquePerUnitTemperature":
        return self._Cast_TorquePerUnitTemperature(self)
