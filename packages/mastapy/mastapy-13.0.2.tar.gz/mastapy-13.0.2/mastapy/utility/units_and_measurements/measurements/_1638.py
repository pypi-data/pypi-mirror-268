"""Decibel"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DECIBEL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Decibel"
)


__docformat__ = "restructuredtext en"
__all__ = ("Decibel",)


Self = TypeVar("Self", bound="Decibel")


class Decibel(_1612.MeasurementBase):
    """Decibel

    This is a mastapy class.
    """

    TYPE = _DECIBEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Decibel")

    class _Cast_Decibel:
        """Special nested class for casting Decibel to subclasses."""

        def __init__(self: "Decibel._Cast_Decibel", parent: "Decibel"):
            self._parent = parent

        @property
        def measurement_base(self: "Decibel._Cast_Decibel") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def decibel(self: "Decibel._Cast_Decibel") -> "Decibel":
            return self._parent

        def __getattr__(self: "Decibel._Cast_Decibel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Decibel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Decibel._Cast_Decibel":
        return self._Cast_Decibel(self)
