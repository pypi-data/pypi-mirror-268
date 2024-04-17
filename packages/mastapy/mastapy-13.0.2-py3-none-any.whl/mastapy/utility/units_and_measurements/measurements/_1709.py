"""PressureViscosityCoefficient"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_VISCOSITY_COEFFICIENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "PressureViscosityCoefficient",
)


__docformat__ = "restructuredtext en"
__all__ = ("PressureViscosityCoefficient",)


Self = TypeVar("Self", bound="PressureViscosityCoefficient")


class PressureViscosityCoefficient(_1612.MeasurementBase):
    """PressureViscosityCoefficient

    This is a mastapy class.
    """

    TYPE = _PRESSURE_VISCOSITY_COEFFICIENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PressureViscosityCoefficient")

    class _Cast_PressureViscosityCoefficient:
        """Special nested class for casting PressureViscosityCoefficient to subclasses."""

        def __init__(
            self: "PressureViscosityCoefficient._Cast_PressureViscosityCoefficient",
            parent: "PressureViscosityCoefficient",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PressureViscosityCoefficient._Cast_PressureViscosityCoefficient",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def pressure_viscosity_coefficient(
            self: "PressureViscosityCoefficient._Cast_PressureViscosityCoefficient",
        ) -> "PressureViscosityCoefficient":
            return self._parent

        def __getattr__(
            self: "PressureViscosityCoefficient._Cast_PressureViscosityCoefficient",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PressureViscosityCoefficient.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PressureViscosityCoefficient._Cast_PressureViscosityCoefficient":
        return self._Cast_PressureViscosityCoefficient(self)
