"""LengthPerUnitTemperature"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_PER_UNIT_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthPerUnitTemperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthPerUnitTemperature",)


Self = TypeVar("Self", bound="LengthPerUnitTemperature")


class LengthPerUnitTemperature(_1612.MeasurementBase):
    """LengthPerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _LENGTH_PER_UNIT_TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthPerUnitTemperature")

    class _Cast_LengthPerUnitTemperature:
        """Special nested class for casting LengthPerUnitTemperature to subclasses."""

        def __init__(
            self: "LengthPerUnitTemperature._Cast_LengthPerUnitTemperature",
            parent: "LengthPerUnitTemperature",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthPerUnitTemperature._Cast_LengthPerUnitTemperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_per_unit_temperature(
            self: "LengthPerUnitTemperature._Cast_LengthPerUnitTemperature",
        ) -> "LengthPerUnitTemperature":
            return self._parent

        def __getattr__(
            self: "LengthPerUnitTemperature._Cast_LengthPerUnitTemperature", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthPerUnitTemperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LengthPerUnitTemperature._Cast_LengthPerUnitTemperature":
        return self._Cast_LengthPerUnitTemperature(self)
