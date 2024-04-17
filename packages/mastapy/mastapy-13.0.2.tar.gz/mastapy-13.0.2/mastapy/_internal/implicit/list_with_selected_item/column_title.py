"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import List, TypeVar

from mastapy.utility.file_access_helpers import _1824
from mastapy._internal import constructor, conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_ColumnTitle",)


Self = TypeVar("Self", bound="ListWithSelectedItem_ColumnTitle")


class ListWithSelectedItem_ColumnTitle(
    _1824.ColumnTitle, mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    """

    __qualname__ = "ColumnTitle"

    def __init__(self, instance_to_wrap: "ListWithSelectedItem_ColumnTitle.TYPE"):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> "_LIST_WITH_SELECTED_ITEM":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> "_1824.ColumnTitle.TYPE":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1824.ColumnTitle.TYPE

    @property
    def selected_value(self: Self) -> "_1824.ColumnTitle":
        """mastapy.utility.file_access_helpers.ColumnTitle

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[_1824.ColumnTitle]":
        """List[mastapy.utility.file_access_helpers.ColumnTitle]

        Note:
            This property is readonly.
        """
        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value
