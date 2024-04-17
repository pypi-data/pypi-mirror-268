"""Angle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Angle"
)


__docformat__ = "restructuredtext en"
__all__ = ("Angle",)


Self = TypeVar("Self", bound="Angle")


class Angle(_1612.MeasurementBase):
    """Angle

    This is a mastapy class.
    """

    TYPE = _ANGLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Angle")

    class _Cast_Angle:
        """Special nested class for casting Angle to subclasses."""

        def __init__(self: "Angle._Cast_Angle", parent: "Angle"):
            self._parent = parent

        @property
        def measurement_base(self: "Angle._Cast_Angle") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angle(self: "Angle._Cast_Angle") -> "Angle":
            return self._parent

        def __getattr__(self: "Angle._Cast_Angle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Angle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Angle._Cast_Angle":
        return self._Cast_Angle(self)
