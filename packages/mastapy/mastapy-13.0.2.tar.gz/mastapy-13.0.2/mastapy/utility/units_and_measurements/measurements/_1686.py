"""MagneticFluxDensity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX_DENSITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MagneticFluxDensity"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagneticFluxDensity",)


Self = TypeVar("Self", bound="MagneticFluxDensity")


class MagneticFluxDensity(_1612.MeasurementBase):
    """MagneticFluxDensity

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FLUX_DENSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagneticFluxDensity")

    class _Cast_MagneticFluxDensity:
        """Special nested class for casting MagneticFluxDensity to subclasses."""

        def __init__(
            self: "MagneticFluxDensity._Cast_MagneticFluxDensity",
            parent: "MagneticFluxDensity",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MagneticFluxDensity._Cast_MagneticFluxDensity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def magnetic_flux_density(
            self: "MagneticFluxDensity._Cast_MagneticFluxDensity",
        ) -> "MagneticFluxDensity":
            return self._parent

        def __getattr__(
            self: "MagneticFluxDensity._Cast_MagneticFluxDensity", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagneticFluxDensity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagneticFluxDensity._Cast_MagneticFluxDensity":
        return self._Cast_MagneticFluxDensity(self)
