"""Gradient"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GRADIENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Gradient"
)


__docformat__ = "restructuredtext en"
__all__ = ("Gradient",)


Self = TypeVar("Self", bound="Gradient")


class Gradient(_1612.MeasurementBase):
    """Gradient

    This is a mastapy class.
    """

    TYPE = _GRADIENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Gradient")

    class _Cast_Gradient:
        """Special nested class for casting Gradient to subclasses."""

        def __init__(self: "Gradient._Cast_Gradient", parent: "Gradient"):
            self._parent = parent

        @property
        def measurement_base(
            self: "Gradient._Cast_Gradient",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def gradient(self: "Gradient._Cast_Gradient") -> "Gradient":
            return self._parent

        def __getattr__(self: "Gradient._Cast_Gradient", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Gradient.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Gradient._Cast_Gradient":
        return self._Cast_Gradient(self)
