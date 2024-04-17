"""Density"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DENSITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Density"
)


__docformat__ = "restructuredtext en"
__all__ = ("Density",)


Self = TypeVar("Self", bound="Density")


class Density(_1612.MeasurementBase):
    """Density

    This is a mastapy class.
    """

    TYPE = _DENSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Density")

    class _Cast_Density:
        """Special nested class for casting Density to subclasses."""

        def __init__(self: "Density._Cast_Density", parent: "Density"):
            self._parent = parent

        @property
        def measurement_base(self: "Density._Cast_Density") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def density(self: "Density._Cast_Density") -> "Density":
            return self._parent

        def __getattr__(self: "Density._Cast_Density", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Density.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Density._Cast_Density":
        return self._Cast_Density(self)
