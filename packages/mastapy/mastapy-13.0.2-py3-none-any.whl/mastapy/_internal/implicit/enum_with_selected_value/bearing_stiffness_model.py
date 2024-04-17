"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BearingStiffnessModel",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BearingStiffnessModel")


class EnumWithSelectedValue_BearingStiffnessModel(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BearingStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingStiffnessModel' types.
    """

    __qualname__ = "BearingStiffnessModel"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5394.BearingStiffnessModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5394.BearingStiffnessModel

    @classmethod
    def implicit_type(cls) -> "_5394.BearingStiffnessModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5394.BearingStiffnessModel.type_()

    @property
    def selected_value(self: Self) -> "_5394.BearingStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingStiffnessModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_5394.BearingStiffnessModel]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BearingStiffnessModel]

        Note:
            This property is readonly.
        """
        return None
