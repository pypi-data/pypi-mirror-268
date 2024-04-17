"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.nodal_analysis.fe_export_utility import _168
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_BoundaryConditionType",)


Self = TypeVar("Self", bound="Overridable_BoundaryConditionType")


class Overridable_BoundaryConditionType(mixins.OverridableMixin, Enum):
    """Overridable_BoundaryConditionType

    A specific implementation of 'Overridable' for 'BoundaryConditionType' types.
    """

    __qualname__ = "BoundaryConditionType"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_168.BoundaryConditionType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _168.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> "_168.BoundaryConditionType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _168.BoundaryConditionType.type_()

    @property
    def value(self: Self) -> "_168.BoundaryConditionType":
        """mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType

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
    def override_value(self: Self) -> "_168.BoundaryConditionType":
        """mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_168.BoundaryConditionType":
        """mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType

        Note:
            This property is readonly.
        """
        return None
