"""ForcePerUnitTemperature"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ForcePerUnitTemperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForcePerUnitTemperature",)


Self = TypeVar("Self", bound="ForcePerUnitTemperature")


class ForcePerUnitTemperature(_1612.MeasurementBase):
    """ForcePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForcePerUnitTemperature")

    class _Cast_ForcePerUnitTemperature:
        """Special nested class for casting ForcePerUnitTemperature to subclasses."""

        def __init__(
            self: "ForcePerUnitTemperature._Cast_ForcePerUnitTemperature",
            parent: "ForcePerUnitTemperature",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ForcePerUnitTemperature._Cast_ForcePerUnitTemperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def force_per_unit_temperature(
            self: "ForcePerUnitTemperature._Cast_ForcePerUnitTemperature",
        ) -> "ForcePerUnitTemperature":
            return self._parent

        def __getattr__(
            self: "ForcePerUnitTemperature._Cast_ForcePerUnitTemperature", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForcePerUnitTemperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ForcePerUnitTemperature._Cast_ForcePerUnitTemperature":
        return self._Cast_ForcePerUnitTemperature(self)
