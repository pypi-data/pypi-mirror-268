"""FractionPerTemperature"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRACTION_PER_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "FractionPerTemperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("FractionPerTemperature",)


Self = TypeVar("Self", bound="FractionPerTemperature")


class FractionPerTemperature(_1612.MeasurementBase):
    """FractionPerTemperature

    This is a mastapy class.
    """

    TYPE = _FRACTION_PER_TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FractionPerTemperature")

    class _Cast_FractionPerTemperature:
        """Special nested class for casting FractionPerTemperature to subclasses."""

        def __init__(
            self: "FractionPerTemperature._Cast_FractionPerTemperature",
            parent: "FractionPerTemperature",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "FractionPerTemperature._Cast_FractionPerTemperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def fraction_per_temperature(
            self: "FractionPerTemperature._Cast_FractionPerTemperature",
        ) -> "FractionPerTemperature":
            return self._parent

        def __getattr__(
            self: "FractionPerTemperature._Cast_FractionPerTemperature", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FractionPerTemperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FractionPerTemperature._Cast_FractionPerTemperature":
        return self._Cast_FractionPerTemperature(self)
