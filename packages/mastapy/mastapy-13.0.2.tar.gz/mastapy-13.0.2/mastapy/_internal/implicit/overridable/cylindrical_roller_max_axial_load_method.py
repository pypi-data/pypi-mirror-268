"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.bearings.bearing_results import _1949
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_CylindricalRollerMaxAxialLoadMethod",)


Self = TypeVar("Self", bound="Overridable_CylindricalRollerMaxAxialLoadMethod")


class Overridable_CylindricalRollerMaxAxialLoadMethod(mixins.OverridableMixin, Enum):
    """Overridable_CylindricalRollerMaxAxialLoadMethod

    A specific implementation of 'Overridable' for 'CylindricalRollerMaxAxialLoadMethod' types.
    """

    __qualname__ = "CylindricalRollerMaxAxialLoadMethod"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1949.CylindricalRollerMaxAxialLoadMethod

    @classmethod
    def implicit_type(cls) -> "_1949.CylindricalRollerMaxAxialLoadMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1949.CylindricalRollerMaxAxialLoadMethod.type_()

    @property
    def value(self: Self) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod

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
    def override_value(self: Self) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod

        Note:
            This property is readonly.
        """
        return None
