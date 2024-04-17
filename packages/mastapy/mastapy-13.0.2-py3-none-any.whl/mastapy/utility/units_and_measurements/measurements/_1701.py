"""PowerSmallPerArea"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_AREA = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "PowerSmallPerArea"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerSmallPerArea",)


Self = TypeVar("Self", bound="PowerSmallPerArea")


class PowerSmallPerArea(_1612.MeasurementBase):
    """PowerSmallPerArea

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_AREA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerSmallPerArea")

    class _Cast_PowerSmallPerArea:
        """Special nested class for casting PowerSmallPerArea to subclasses."""

        def __init__(
            self: "PowerSmallPerArea._Cast_PowerSmallPerArea",
            parent: "PowerSmallPerArea",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerSmallPerArea._Cast_PowerSmallPerArea",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_small_per_area(
            self: "PowerSmallPerArea._Cast_PowerSmallPerArea",
        ) -> "PowerSmallPerArea":
            return self._parent

        def __getattr__(self: "PowerSmallPerArea._Cast_PowerSmallPerArea", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerSmallPerArea.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PowerSmallPerArea._Cast_PowerSmallPerArea":
        return self._Cast_PowerSmallPerArea(self)
