"""PowerSmallPerMass"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_MASS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PowerSmallPerMass"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerSmallPerMass",)


Self = TypeVar("Self", bound="PowerSmallPerMass")


class PowerSmallPerMass(_1612.MeasurementBase):
    """PowerSmallPerMass

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_MASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerSmallPerMass")

    class _Cast_PowerSmallPerMass:
        """Special nested class for casting PowerSmallPerMass to subclasses."""

        def __init__(
            self: "PowerSmallPerMass._Cast_PowerSmallPerMass",
            parent: "PowerSmallPerMass",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerSmallPerMass._Cast_PowerSmallPerMass",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_small_per_mass(
            self: "PowerSmallPerMass._Cast_PowerSmallPerMass",
        ) -> "PowerSmallPerMass":
            return self._parent

        def __getattr__(self: "PowerSmallPerMass._Cast_PowerSmallPerMass", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerSmallPerMass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PowerSmallPerMass._Cast_PowerSmallPerMass":
        return self._Cast_PowerSmallPerMass(self)
