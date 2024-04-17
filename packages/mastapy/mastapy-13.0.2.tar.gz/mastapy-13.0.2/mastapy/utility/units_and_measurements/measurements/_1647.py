"""Enum"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENUM = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Enum"
)


__docformat__ = "restructuredtext en"
__all__ = ("Enum",)


Self = TypeVar("Self", bound="Enum")


class Enum(_1612.MeasurementBase):
    """Enum

    This is a mastapy class.
    """

    TYPE = _ENUM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Enum")

    class _Cast_Enum:
        """Special nested class for casting Enum to subclasses."""

        def __init__(self: "Enum._Cast_Enum", parent: "Enum"):
            self._parent = parent

        @property
        def measurement_base(self: "Enum._Cast_Enum") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def enum(self: "Enum._Cast_Enum") -> "Enum":
            return self._parent

        def __getattr__(self: "Enum._Cast_Enum", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Enum.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Enum._Cast_Enum":
        return self._Cast_Enum(self)
