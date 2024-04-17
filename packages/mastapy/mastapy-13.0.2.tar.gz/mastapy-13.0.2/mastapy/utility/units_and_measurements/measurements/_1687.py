"""MagneticVectorPotential"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_VECTOR_POTENTIAL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MagneticVectorPotential"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagneticVectorPotential",)


Self = TypeVar("Self", bound="MagneticVectorPotential")


class MagneticVectorPotential(_1612.MeasurementBase):
    """MagneticVectorPotential

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_VECTOR_POTENTIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagneticVectorPotential")

    class _Cast_MagneticVectorPotential:
        """Special nested class for casting MagneticVectorPotential to subclasses."""

        def __init__(
            self: "MagneticVectorPotential._Cast_MagneticVectorPotential",
            parent: "MagneticVectorPotential",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MagneticVectorPotential._Cast_MagneticVectorPotential",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def magnetic_vector_potential(
            self: "MagneticVectorPotential._Cast_MagneticVectorPotential",
        ) -> "MagneticVectorPotential":
            return self._parent

        def __getattr__(
            self: "MagneticVectorPotential._Cast_MagneticVectorPotential", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagneticVectorPotential.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagneticVectorPotential._Cast_MagneticVectorPotential":
        return self._Cast_MagneticVectorPotential(self)
