"""ThermalContactCoefficient"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_CONTACT_COEFFICIENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "ThermalContactCoefficient",
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermalContactCoefficient",)


Self = TypeVar("Self", bound="ThermalContactCoefficient")


class ThermalContactCoefficient(_1612.MeasurementBase):
    """ThermalContactCoefficient

    This is a mastapy class.
    """

    TYPE = _THERMAL_CONTACT_COEFFICIENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThermalContactCoefficient")

    class _Cast_ThermalContactCoefficient:
        """Special nested class for casting ThermalContactCoefficient to subclasses."""

        def __init__(
            self: "ThermalContactCoefficient._Cast_ThermalContactCoefficient",
            parent: "ThermalContactCoefficient",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ThermalContactCoefficient._Cast_ThermalContactCoefficient",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def thermal_contact_coefficient(
            self: "ThermalContactCoefficient._Cast_ThermalContactCoefficient",
        ) -> "ThermalContactCoefficient":
            return self._parent

        def __getattr__(
            self: "ThermalContactCoefficient._Cast_ThermalContactCoefficient", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThermalContactCoefficient.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ThermalContactCoefficient._Cast_ThermalContactCoefficient":
        return self._Cast_ThermalContactCoefficient(self)
