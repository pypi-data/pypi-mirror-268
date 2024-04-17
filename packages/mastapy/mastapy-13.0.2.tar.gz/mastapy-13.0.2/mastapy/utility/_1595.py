"""IntegerRange"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTEGER_RANGE = python_net_import("SMT.MastaAPI.Utility", "IntegerRange")


__docformat__ = "restructuredtext en"
__all__ = ("IntegerRange",)


Self = TypeVar("Self", bound="IntegerRange")


class IntegerRange(_0.APIBase):
    """IntegerRange

    This is a mastapy class.
    """

    TYPE = _INTEGER_RANGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IntegerRange")

    class _Cast_IntegerRange:
        """Special nested class for casting IntegerRange to subclasses."""

        def __init__(self: "IntegerRange._Cast_IntegerRange", parent: "IntegerRange"):
            self._parent = parent

        @property
        def integer_range(self: "IntegerRange._Cast_IntegerRange") -> "IntegerRange":
            return self._parent

        def __getattr__(self: "IntegerRange._Cast_IntegerRange", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "IntegerRange.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Max

        if temp is None:
            return 0

        return temp

    @max.setter
    @enforce_parameter_types
    def max(self: Self, value: "int"):
        self.wrapped.Max = int(value) if value is not None else 0

    @property
    def min(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Min

        if temp is None:
            return 0

        return temp

    @min.setter
    @enforce_parameter_types
    def min(self: Self, value: "int"):
        self.wrapped.Min = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "IntegerRange._Cast_IntegerRange":
        return self._Cast_IntegerRange(self)
