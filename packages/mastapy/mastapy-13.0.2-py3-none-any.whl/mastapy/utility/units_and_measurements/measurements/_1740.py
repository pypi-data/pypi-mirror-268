"""Viscosity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VISCOSITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Viscosity"
)


__docformat__ = "restructuredtext en"
__all__ = ("Viscosity",)


Self = TypeVar("Self", bound="Viscosity")


class Viscosity(_1612.MeasurementBase):
    """Viscosity

    This is a mastapy class.
    """

    TYPE = _VISCOSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Viscosity")

    class _Cast_Viscosity:
        """Special nested class for casting Viscosity to subclasses."""

        def __init__(self: "Viscosity._Cast_Viscosity", parent: "Viscosity"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Viscosity._Cast_Viscosity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def viscosity(self: "Viscosity._Cast_Viscosity") -> "Viscosity":
            return self._parent

        def __getattr__(self: "Viscosity._Cast_Viscosity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Viscosity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Viscosity._Cast_Viscosity":
        return self._Cast_Viscosity(self)
