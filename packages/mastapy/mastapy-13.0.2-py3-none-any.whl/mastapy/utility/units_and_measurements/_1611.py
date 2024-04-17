"""InverseUnit"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_UNIT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "InverseUnit"
)


__docformat__ = "restructuredtext en"
__all__ = ("InverseUnit",)


Self = TypeVar("Self", bound="InverseUnit")


class InverseUnit(_1617.Unit):
    """InverseUnit

    This is a mastapy class.
    """

    TYPE = _INVERSE_UNIT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InverseUnit")

    class _Cast_InverseUnit:
        """Special nested class for casting InverseUnit to subclasses."""

        def __init__(self: "InverseUnit._Cast_InverseUnit", parent: "InverseUnit"):
            self._parent = parent

        @property
        def unit(self: "InverseUnit._Cast_InverseUnit") -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def inverse_unit(self: "InverseUnit._Cast_InverseUnit") -> "InverseUnit":
            return self._parent

        def __getattr__(self: "InverseUnit._Cast_InverseUnit", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InverseUnit.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InverseUnit._Cast_InverseUnit":
        return self._Cast_InverseUnit(self)
