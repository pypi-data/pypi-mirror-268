"""PowerSmallPerUnitAreaPerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_UNIT_AREA_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "PowerSmallPerUnitAreaPerUnitTime",
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerSmallPerUnitAreaPerUnitTime",)


Self = TypeVar("Self", bound="PowerSmallPerUnitAreaPerUnitTime")


class PowerSmallPerUnitAreaPerUnitTime(_1612.MeasurementBase):
    """PowerSmallPerUnitAreaPerUnitTime

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_UNIT_AREA_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerSmallPerUnitAreaPerUnitTime")

    class _Cast_PowerSmallPerUnitAreaPerUnitTime:
        """Special nested class for casting PowerSmallPerUnitAreaPerUnitTime to subclasses."""

        def __init__(
            self: "PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime",
            parent: "PowerSmallPerUnitAreaPerUnitTime",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def power_small_per_unit_area_per_unit_time(
            self: "PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime",
        ) -> "PowerSmallPerUnitAreaPerUnitTime":
            return self._parent

        def __getattr__(
            self: "PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerSmallPerUnitAreaPerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime":
        return self._Cast_PowerSmallPerUnitAreaPerUnitTime(self)
