"""LengthVeryLong"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_VERY_LONG = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthVeryLong"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthVeryLong",)


Self = TypeVar("Self", bound="LengthVeryLong")


class LengthVeryLong(_1612.MeasurementBase):
    """LengthVeryLong

    This is a mastapy class.
    """

    TYPE = _LENGTH_VERY_LONG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthVeryLong")

    class _Cast_LengthVeryLong:
        """Special nested class for casting LengthVeryLong to subclasses."""

        def __init__(
            self: "LengthVeryLong._Cast_LengthVeryLong", parent: "LengthVeryLong"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthVeryLong._Cast_LengthVeryLong",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_very_long(
            self: "LengthVeryLong._Cast_LengthVeryLong",
        ) -> "LengthVeryLong":
            return self._parent

        def __getattr__(self: "LengthVeryLong._Cast_LengthVeryLong", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthVeryLong.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LengthVeryLong._Cast_LengthVeryLong":
        return self._Cast_LengthVeryLong(self)
