"""EnumUnit"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENUM_UNIT = python_net_import("SMT.MastaAPI.Utility.UnitsAndMeasurements", "EnumUnit")


__docformat__ = "restructuredtext en"
__all__ = ("EnumUnit",)


Self = TypeVar("Self", bound="EnumUnit")


class EnumUnit(_1617.Unit):
    """EnumUnit

    This is a mastapy class.
    """

    TYPE = _ENUM_UNIT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnumUnit")

    class _Cast_EnumUnit:
        """Special nested class for casting EnumUnit to subclasses."""

        def __init__(self: "EnumUnit._Cast_EnumUnit", parent: "EnumUnit"):
            self._parent = parent

        @property
        def unit(self: "EnumUnit._Cast_EnumUnit") -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def enum_unit(self: "EnumUnit._Cast_EnumUnit") -> "EnumUnit":
            return self._parent

        def __getattr__(self: "EnumUnit._Cast_EnumUnit", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnumUnit.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "EnumUnit._Cast_EnumUnit":
        return self._Cast_EnumUnit(self)
