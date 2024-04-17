"""LengthMedium"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_MEDIUM = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthMedium"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthMedium",)


Self = TypeVar("Self", bound="LengthMedium")


class LengthMedium(_1612.MeasurementBase):
    """LengthMedium

    This is a mastapy class.
    """

    TYPE = _LENGTH_MEDIUM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthMedium")

    class _Cast_LengthMedium:
        """Special nested class for casting LengthMedium to subclasses."""

        def __init__(self: "LengthMedium._Cast_LengthMedium", parent: "LengthMedium"):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthMedium._Cast_LengthMedium",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_medium(self: "LengthMedium._Cast_LengthMedium") -> "LengthMedium":
            return self._parent

        def __getattr__(self: "LengthMedium._Cast_LengthMedium", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthMedium.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LengthMedium._Cast_LengthMedium":
        return self._Cast_LengthMedium(self)
