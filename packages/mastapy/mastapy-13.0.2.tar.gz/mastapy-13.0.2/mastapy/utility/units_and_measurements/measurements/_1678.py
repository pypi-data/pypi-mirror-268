"""LengthVeryShortPerLengthShort"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_VERY_SHORT_PER_LENGTH_SHORT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "LengthVeryShortPerLengthShort",
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthVeryShortPerLengthShort",)


Self = TypeVar("Self", bound="LengthVeryShortPerLengthShort")


class LengthVeryShortPerLengthShort(_1612.MeasurementBase):
    """LengthVeryShortPerLengthShort

    This is a mastapy class.
    """

    TYPE = _LENGTH_VERY_SHORT_PER_LENGTH_SHORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthVeryShortPerLengthShort")

    class _Cast_LengthVeryShortPerLengthShort:
        """Special nested class for casting LengthVeryShortPerLengthShort to subclasses."""

        def __init__(
            self: "LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort",
            parent: "LengthVeryShortPerLengthShort",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_very_short_per_length_short(
            self: "LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort",
        ) -> "LengthVeryShortPerLengthShort":
            return self._parent

        def __getattr__(
            self: "LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthVeryShortPerLengthShort.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort":
        return self._Cast_LengthVeryShortPerLengthShort(self)
