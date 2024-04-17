"""UnitGradient"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNIT_GRADIENT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "UnitGradient"
)


__docformat__ = "restructuredtext en"
__all__ = ("UnitGradient",)


Self = TypeVar("Self", bound="UnitGradient")


class UnitGradient(_1617.Unit):
    """UnitGradient

    This is a mastapy class.
    """

    TYPE = _UNIT_GRADIENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnitGradient")

    class _Cast_UnitGradient:
        """Special nested class for casting UnitGradient to subclasses."""

        def __init__(self: "UnitGradient._Cast_UnitGradient", parent: "UnitGradient"):
            self._parent = parent

        @property
        def unit(self: "UnitGradient._Cast_UnitGradient") -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def unit_gradient(self: "UnitGradient._Cast_UnitGradient") -> "UnitGradient":
            return self._parent

        def __getattr__(self: "UnitGradient._Cast_UnitGradient", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnitGradient.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "UnitGradient._Cast_UnitGradient":
        return self._Cast_UnitGradient(self)
