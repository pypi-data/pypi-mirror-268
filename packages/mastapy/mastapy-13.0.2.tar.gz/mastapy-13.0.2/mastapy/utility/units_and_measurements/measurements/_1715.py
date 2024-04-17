"""Rotatum"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTATUM = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Rotatum"
)


__docformat__ = "restructuredtext en"
__all__ = ("Rotatum",)


Self = TypeVar("Self", bound="Rotatum")


class Rotatum(_1612.MeasurementBase):
    """Rotatum

    This is a mastapy class.
    """

    TYPE = _ROTATUM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Rotatum")

    class _Cast_Rotatum:
        """Special nested class for casting Rotatum to subclasses."""

        def __init__(self: "Rotatum._Cast_Rotatum", parent: "Rotatum"):
            self._parent = parent

        @property
        def measurement_base(self: "Rotatum._Cast_Rotatum") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def rotatum(self: "Rotatum._Cast_Rotatum") -> "Rotatum":
            return self._parent

        def __getattr__(self: "Rotatum._Cast_Rotatum", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Rotatum.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Rotatum._Cast_Rotatum":
        return self._Cast_Rotatum(self)
