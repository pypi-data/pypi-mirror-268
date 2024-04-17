"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.part_model import _2482
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing",)


Self = TypeVar(
    "Self",
    bound="EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing",
)


class EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftDiameterModificationDueToRollingBearingRing' types.
    """

    __qualname__ = "ShaftDiameterModificationDueToRollingBearingRing"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2482.ShaftDiameterModificationDueToRollingBearingRing":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2482.ShaftDiameterModificationDueToRollingBearingRing

    @classmethod
    def implicit_type(
        cls,
    ) -> "_2482.ShaftDiameterModificationDueToRollingBearingRing.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2482.ShaftDiameterModificationDueToRollingBearingRing.type_()

    @property
    def selected_value(
        self: Self,
    ) -> "_2482.ShaftDiameterModificationDueToRollingBearingRing":
        """mastapy.system_model.part_model.ShaftDiameterModificationDueToRollingBearingRing

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_2482.ShaftDiameterModificationDueToRollingBearingRing]":
        """List[mastapy.system_model.part_model.ShaftDiameterModificationDueToRollingBearingRing]

        Note:
            This property is readonly.
        """
        return None
