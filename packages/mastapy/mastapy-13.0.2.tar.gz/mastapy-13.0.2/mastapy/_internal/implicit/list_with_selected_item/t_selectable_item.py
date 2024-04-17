"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import List, Generic, TypeVar

from mastapy._internal import constructor, conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_TSelectableItem",)


Self = TypeVar("Self", bound="ListWithSelectedItem_TSelectableItem")
TSelectableItem = TypeVar("TSelectableItem")


class ListWithSelectedItem_TSelectableItem(
    Generic[TSelectableItem], mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    """

    __qualname__ = "TSelectableItem"

    def __init__(self, instance_to_wrap: "ListWithSelectedItem_TSelectableItem.TYPE"):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> "_LIST_WITH_SELECTED_ITEM":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> "TSelectableItem":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TSelectableItem

    @property
    def selected_value(self: Self) -> "TSelectableItem":
        """TSelectableItem

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[TSelectableItem]":
        """List[TSelectableItem]

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
