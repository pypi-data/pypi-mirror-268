"""PricePerUnitMass"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRICE_PER_UNIT_MASS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PricePerUnitMass"
)


__docformat__ = "restructuredtext en"
__all__ = ("PricePerUnitMass",)


Self = TypeVar("Self", bound="PricePerUnitMass")


class PricePerUnitMass(_1612.MeasurementBase):
    """PricePerUnitMass

    This is a mastapy class.
    """

    TYPE = _PRICE_PER_UNIT_MASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PricePerUnitMass")

    class _Cast_PricePerUnitMass:
        """Special nested class for casting PricePerUnitMass to subclasses."""

        def __init__(
            self: "PricePerUnitMass._Cast_PricePerUnitMass", parent: "PricePerUnitMass"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PricePerUnitMass._Cast_PricePerUnitMass",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def price_per_unit_mass(
            self: "PricePerUnitMass._Cast_PricePerUnitMass",
        ) -> "PricePerUnitMass":
            return self._parent

        def __getattr__(self: "PricePerUnitMass._Cast_PricePerUnitMass", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PricePerUnitMass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PricePerUnitMass._Cast_PricePerUnitMass":
        return self._Cast_PricePerUnitMass(self)
