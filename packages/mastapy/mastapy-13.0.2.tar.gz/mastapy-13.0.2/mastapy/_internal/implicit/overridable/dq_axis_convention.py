"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.electric_machines import _1266
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_DQAxisConvention",)


Self = TypeVar("Self", bound="Overridable_DQAxisConvention")


class Overridable_DQAxisConvention(mixins.OverridableMixin, Enum):
    """Overridable_DQAxisConvention

    A specific implementation of 'Overridable' for 'DQAxisConvention' types.
    """

    __qualname__ = "DQAxisConvention"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_1266.DQAxisConvention":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1266.DQAxisConvention

    @classmethod
    def implicit_type(cls) -> "_1266.DQAxisConvention.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1266.DQAxisConvention.type_()

    @property
    def value(self: Self) -> "_1266.DQAxisConvention":
        """mastapy.electric_machines.DQAxisConvention

        Note:
            This property is readonly.
        """
        return None

    @property
    def overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        return None

    @property
    def override_value(self: Self) -> "_1266.DQAxisConvention":
        """mastapy.electric_machines.DQAxisConvention

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_1266.DQAxisConvention":
        """mastapy.electric_machines.DQAxisConvention

        Note:
            This property is readonly.
        """
        return None
