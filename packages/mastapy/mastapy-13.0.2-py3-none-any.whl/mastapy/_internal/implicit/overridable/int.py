"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_int",)


Self = TypeVar("Self", bound="Overridable_int")


class Overridable_int(int, mixins.OverridableMixin):
    """Overridable_int

    A specific implementation of 'Overridable' for 'int' types.
    """

    __qualname__ = "int"

    def __new__(cls, instance_to_wrap: "Overridable_int.TYPE"):
        return int.__new__(
            cls, instance_to_wrap.Value if instance_to_wrap.Value is not None else 0
        )

    def __init__(self, instance_to_wrap: "Overridable_int.TYPE"):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.Value
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def implicit_type(cls) -> "int":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def value(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.enclosing.Value

        if temp is None:
            return 0

        return temp

    @property
    def overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.enclosing.Overridden

        if temp is None:
            return False

        return temp

    @property
    def override_value(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.enclosing.OverrideValue

        if temp is None:
            return 0

        return temp

    @property
    def calculated_value(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.enclosing.CalculatedValue

        if temp is None:
            return 0

        return temp
