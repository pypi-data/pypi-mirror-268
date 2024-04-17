"""PowerSmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PowerSmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerSmall",)


Self = TypeVar("Self", bound="PowerSmall")


class PowerSmall(_1612.MeasurementBase):
    """PowerSmall

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerSmall")

    class _Cast_PowerSmall:
        """Special nested class for casting PowerSmall to subclasses."""

        def __init__(self: "PowerSmall._Cast_PowerSmall", parent: "PowerSmall"):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerSmall._Cast_PowerSmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_small(self: "PowerSmall._Cast_PowerSmall") -> "PowerSmall":
            return self._parent

        def __getattr__(self: "PowerSmall._Cast_PowerSmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerSmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PowerSmall._Cast_PowerSmall":
        return self._Cast_PowerSmall(self)
