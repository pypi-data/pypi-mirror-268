"""Jerk"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_JERK = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Jerk"
)


__docformat__ = "restructuredtext en"
__all__ = ("Jerk",)


Self = TypeVar("Self", bound="Jerk")


class Jerk(_1612.MeasurementBase):
    """Jerk

    This is a mastapy class.
    """

    TYPE = _JERK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Jerk")

    class _Cast_Jerk:
        """Special nested class for casting Jerk to subclasses."""

        def __init__(self: "Jerk._Cast_Jerk", parent: "Jerk"):
            self._parent = parent

        @property
        def measurement_base(self: "Jerk._Cast_Jerk") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def jerk(self: "Jerk._Cast_Jerk") -> "Jerk":
            return self._parent

        def __getattr__(self: "Jerk._Cast_Jerk", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Jerk.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Jerk._Cast_Jerk":
        return self._Cast_Jerk(self)
