"""Acceleration"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACCELERATION = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Acceleration"
)


__docformat__ = "restructuredtext en"
__all__ = ("Acceleration",)


Self = TypeVar("Self", bound="Acceleration")


class Acceleration(_1612.MeasurementBase):
    """Acceleration

    This is a mastapy class.
    """

    TYPE = _ACCELERATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Acceleration")

    class _Cast_Acceleration:
        """Special nested class for casting Acceleration to subclasses."""

        def __init__(self: "Acceleration._Cast_Acceleration", parent: "Acceleration"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Acceleration._Cast_Acceleration",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def acceleration(self: "Acceleration._Cast_Acceleration") -> "Acceleration":
            return self._parent

        def __getattr__(self: "Acceleration._Cast_Acceleration", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Acceleration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Acceleration._Cast_Acceleration":
        return self._Cast_Acceleration(self)
