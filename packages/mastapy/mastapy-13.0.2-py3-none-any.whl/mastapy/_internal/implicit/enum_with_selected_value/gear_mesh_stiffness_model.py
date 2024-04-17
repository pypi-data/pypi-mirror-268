"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses import _5446
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_GearMeshStiffnessModel",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_GearMeshStiffnessModel")


class EnumWithSelectedValue_GearMeshStiffnessModel(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_GearMeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'GearMeshStiffnessModel' types.
    """

    __qualname__ = "GearMeshStiffnessModel"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5446.GearMeshStiffnessModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5446.GearMeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> "_5446.GearMeshStiffnessModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5446.GearMeshStiffnessModel.type_()

    @property
    def selected_value(self: Self) -> "_5446.GearMeshStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_5446.GearMeshStiffnessModel]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel]

        Note:
            This property is readonly.
        """
        return None
