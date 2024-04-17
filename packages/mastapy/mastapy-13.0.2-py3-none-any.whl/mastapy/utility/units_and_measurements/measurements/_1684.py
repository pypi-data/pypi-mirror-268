"""MagneticFieldStrength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FIELD_STRENGTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MagneticFieldStrength"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagneticFieldStrength",)


Self = TypeVar("Self", bound="MagneticFieldStrength")


class MagneticFieldStrength(_1612.MeasurementBase):
    """MagneticFieldStrength

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FIELD_STRENGTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagneticFieldStrength")

    class _Cast_MagneticFieldStrength:
        """Special nested class for casting MagneticFieldStrength to subclasses."""

        def __init__(
            self: "MagneticFieldStrength._Cast_MagneticFieldStrength",
            parent: "MagneticFieldStrength",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MagneticFieldStrength._Cast_MagneticFieldStrength",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def magnetic_field_strength(
            self: "MagneticFieldStrength._Cast_MagneticFieldStrength",
        ) -> "MagneticFieldStrength":
            return self._parent

        def __getattr__(
            self: "MagneticFieldStrength._Cast_MagneticFieldStrength", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagneticFieldStrength.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagneticFieldStrength._Cast_MagneticFieldStrength":
        return self._Cast_MagneticFieldStrength(self)
