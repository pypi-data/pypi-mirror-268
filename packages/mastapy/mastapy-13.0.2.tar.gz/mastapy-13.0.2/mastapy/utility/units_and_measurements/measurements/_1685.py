"""MagneticFlux"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MagneticFlux"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagneticFlux",)


Self = TypeVar("Self", bound="MagneticFlux")


class MagneticFlux(_1612.MeasurementBase):
    """MagneticFlux

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FLUX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagneticFlux")

    class _Cast_MagneticFlux:
        """Special nested class for casting MagneticFlux to subclasses."""

        def __init__(self: "MagneticFlux._Cast_MagneticFlux", parent: "MagneticFlux"):
            self._parent = parent

        @property
        def measurement_base(
            self: "MagneticFlux._Cast_MagneticFlux",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def magnetic_flux(self: "MagneticFlux._Cast_MagneticFlux") -> "MagneticFlux":
            return self._parent

        def __getattr__(self: "MagneticFlux._Cast_MagneticFlux", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagneticFlux.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagneticFlux._Cast_MagneticFlux":
        return self._Cast_MagneticFlux(self)
