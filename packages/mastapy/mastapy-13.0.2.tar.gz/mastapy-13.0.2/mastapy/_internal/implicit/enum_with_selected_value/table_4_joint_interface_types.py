"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.interference_fits import _1455
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_Table4JointInterfaceTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_Table4JointInterfaceTypes")


class EnumWithSelectedValue_Table4JointInterfaceTypes(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_Table4JointInterfaceTypes

    A specific implementation of 'EnumWithSelectedValue' for 'Table4JointInterfaceTypes' types.
    """

    __qualname__ = "Table4JointInterfaceTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1455.Table4JointInterfaceTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1455.Table4JointInterfaceTypes

    @classmethod
    def implicit_type(cls) -> "_1455.Table4JointInterfaceTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1455.Table4JointInterfaceTypes.type_()

    @property
    def selected_value(self: Self) -> "_1455.Table4JointInterfaceTypes":
        """mastapy.detailed_rigid_connectors.interference_fits.Table4JointInterfaceTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1455.Table4JointInterfaceTypes]":
        """List[mastapy.detailed_rigid_connectors.interference_fits.Table4JointInterfaceTypes]

        Note:
            This property is readonly.
        """
        return None
