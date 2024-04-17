"""LengthVeryShort"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_VERY_SHORT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthVeryShort"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthVeryShort",)


Self = TypeVar("Self", bound="LengthVeryShort")


class LengthVeryShort(_1612.MeasurementBase):
    """LengthVeryShort

    This is a mastapy class.
    """

    TYPE = _LENGTH_VERY_SHORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthVeryShort")

    class _Cast_LengthVeryShort:
        """Special nested class for casting LengthVeryShort to subclasses."""

        def __init__(
            self: "LengthVeryShort._Cast_LengthVeryShort", parent: "LengthVeryShort"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthVeryShort._Cast_LengthVeryShort",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_very_short(
            self: "LengthVeryShort._Cast_LengthVeryShort",
        ) -> "LengthVeryShort":
            return self._parent

        def __getattr__(self: "LengthVeryShort._Cast_LengthVeryShort", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthVeryShort.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LengthVeryShort._Cast_LengthVeryShort":
        return self._Cast_LengthVeryShort(self)
