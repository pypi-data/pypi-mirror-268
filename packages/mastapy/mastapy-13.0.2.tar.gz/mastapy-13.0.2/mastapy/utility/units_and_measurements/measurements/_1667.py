"""InverseShortLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_SHORT_LENGTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "InverseShortLength"
)


__docformat__ = "restructuredtext en"
__all__ = ("InverseShortLength",)


Self = TypeVar("Self", bound="InverseShortLength")


class InverseShortLength(_1612.MeasurementBase):
    """InverseShortLength

    This is a mastapy class.
    """

    TYPE = _INVERSE_SHORT_LENGTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InverseShortLength")

    class _Cast_InverseShortLength:
        """Special nested class for casting InverseShortLength to subclasses."""

        def __init__(
            self: "InverseShortLength._Cast_InverseShortLength",
            parent: "InverseShortLength",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "InverseShortLength._Cast_InverseShortLength",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def inverse_short_length(
            self: "InverseShortLength._Cast_InverseShortLength",
        ) -> "InverseShortLength":
            return self._parent

        def __getattr__(self: "InverseShortLength._Cast_InverseShortLength", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InverseShortLength.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InverseShortLength._Cast_InverseShortLength":
        return self._Cast_InverseShortLength(self)
