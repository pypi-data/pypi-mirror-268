"""CarbonEmissionFactor"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CARBON_EMISSION_FACTOR = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "CarbonEmissionFactor"
)


__docformat__ = "restructuredtext en"
__all__ = ("CarbonEmissionFactor",)


Self = TypeVar("Self", bound="CarbonEmissionFactor")


class CarbonEmissionFactor(_1612.MeasurementBase):
    """CarbonEmissionFactor

    This is a mastapy class.
    """

    TYPE = _CARBON_EMISSION_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CarbonEmissionFactor")

    class _Cast_CarbonEmissionFactor:
        """Special nested class for casting CarbonEmissionFactor to subclasses."""

        def __init__(
            self: "CarbonEmissionFactor._Cast_CarbonEmissionFactor",
            parent: "CarbonEmissionFactor",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "CarbonEmissionFactor._Cast_CarbonEmissionFactor",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def carbon_emission_factor(
            self: "CarbonEmissionFactor._Cast_CarbonEmissionFactor",
        ) -> "CarbonEmissionFactor":
            return self._parent

        def __getattr__(
            self: "CarbonEmissionFactor._Cast_CarbonEmissionFactor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CarbonEmissionFactor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CarbonEmissionFactor._Cast_CarbonEmissionFactor":
        return self._Cast_CarbonEmissionFactor(self)
