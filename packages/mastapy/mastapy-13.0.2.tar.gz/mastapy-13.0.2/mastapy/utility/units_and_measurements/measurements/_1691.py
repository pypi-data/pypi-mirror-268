"""MassPerUnitTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_PER_UNIT_TIME = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MassPerUnitTime"
)


__docformat__ = "restructuredtext en"
__all__ = ("MassPerUnitTime",)


Self = TypeVar("Self", bound="MassPerUnitTime")


class MassPerUnitTime(_1612.MeasurementBase):
    """MassPerUnitTime

    This is a mastapy class.
    """

    TYPE = _MASS_PER_UNIT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassPerUnitTime")

    class _Cast_MassPerUnitTime:
        """Special nested class for casting MassPerUnitTime to subclasses."""

        def __init__(
            self: "MassPerUnitTime._Cast_MassPerUnitTime", parent: "MassPerUnitTime"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MassPerUnitTime._Cast_MassPerUnitTime",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def mass_per_unit_time(
            self: "MassPerUnitTime._Cast_MassPerUnitTime",
        ) -> "MassPerUnitTime":
            return self._parent

        def __getattr__(self: "MassPerUnitTime._Cast_MassPerUnitTime", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassPerUnitTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MassPerUnitTime._Cast_MassPerUnitTime":
        return self._Cast_MassPerUnitTime(self)
