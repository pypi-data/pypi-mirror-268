"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from mastapy._internal import constructor, mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_T",)


Self = TypeVar("Self", bound="Overridable_T")
T = TypeVar("T")


class Overridable_T(Generic[T], mixins.OverridableMixin):
    """Overridable_T

    A specific implementation of 'Overridable' for 'T' types.
    """

    __qualname__ = "T"

    def __init__(self, instance_to_wrap: "Overridable_T.TYPE"):
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
    def implicit_type(cls) -> "T":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def value(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.enclosing.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def override_value(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.enclosing.OverrideValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def calculated_value(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.enclosing.CalculatedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)
