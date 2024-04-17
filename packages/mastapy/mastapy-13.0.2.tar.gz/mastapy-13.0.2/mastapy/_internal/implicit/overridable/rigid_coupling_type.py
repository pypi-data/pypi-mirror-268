"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _205
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_RigidCouplingType",)


Self = TypeVar("Self", bound="Overridable_RigidCouplingType")


class Overridable_RigidCouplingType(mixins.OverridableMixin, Enum):
    """Overridable_RigidCouplingType

    A specific implementation of 'Overridable' for 'RigidCouplingType' types.
    """

    __qualname__ = "RigidCouplingType"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_205.RigidCouplingType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _205.RigidCouplingType

    @classmethod
    def implicit_type(cls) -> "_205.RigidCouplingType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _205.RigidCouplingType.type_()

    @property
    def value(self: Self) -> "_205.RigidCouplingType":
        """mastapy.nodal_analysis.dev_tools_analyses.RigidCouplingType

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
    def override_value(self: Self) -> "_205.RigidCouplingType":
        """mastapy.nodal_analysis.dev_tools_analyses.RigidCouplingType

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_205.RigidCouplingType":
        """mastapy.nodal_analysis.dev_tools_analyses.RigidCouplingType

        Note:
            This property is readonly.
        """
        return None
