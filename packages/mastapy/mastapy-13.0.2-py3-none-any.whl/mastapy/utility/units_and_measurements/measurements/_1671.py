"""LengthLong"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_LONG = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthLong"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthLong",)


Self = TypeVar("Self", bound="LengthLong")


class LengthLong(_1612.MeasurementBase):
    """LengthLong

    This is a mastapy class.
    """

    TYPE = _LENGTH_LONG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthLong")

    class _Cast_LengthLong:
        """Special nested class for casting LengthLong to subclasses."""

        def __init__(self: "LengthLong._Cast_LengthLong", parent: "LengthLong"):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthLong._Cast_LengthLong",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_long(self: "LengthLong._Cast_LengthLong") -> "LengthLong":
            return self._parent

        def __getattr__(self: "LengthLong._Cast_LengthLong", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthLong.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LengthLong._Cast_LengthLong":
        return self._Cast_LengthLong(self)
