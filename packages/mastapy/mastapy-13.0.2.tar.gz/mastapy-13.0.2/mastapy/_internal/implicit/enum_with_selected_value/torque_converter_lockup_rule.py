"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses import _5517
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_TorqueConverterLockupRule",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_TorqueConverterLockupRule")


class EnumWithSelectedValue_TorqueConverterLockupRule(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_TorqueConverterLockupRule

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueConverterLockupRule' types.
    """

    __qualname__ = "TorqueConverterLockupRule"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5517.TorqueConverterLockupRule":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5517.TorqueConverterLockupRule

    @classmethod
    def implicit_type(cls) -> "_5517.TorqueConverterLockupRule.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5517.TorqueConverterLockupRule.type_()

    @property
    def selected_value(self: Self) -> "_5517.TorqueConverterLockupRule":
        """mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterLockupRule

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_5517.TorqueConverterLockupRule]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterLockupRule]

        Note:
            This property is readonly.
        """
        return None
