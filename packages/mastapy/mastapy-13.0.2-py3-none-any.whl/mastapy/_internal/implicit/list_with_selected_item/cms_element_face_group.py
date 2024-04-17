"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import List, TypeVar

from mastapy.nodal_analysis.component_mode_synthesis import _227
from mastapy._internal import constructor, conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_CMSElementFaceGroup",)


Self = TypeVar("Self", bound="ListWithSelectedItem_CMSElementFaceGroup")


class ListWithSelectedItem_CMSElementFaceGroup(
    _227.CMSElementFaceGroup, mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_CMSElementFaceGroup

    A specific implementation of 'ListWithSelectedItem' for 'CMSElementFaceGroup' types.
    """

    __qualname__ = "CMSElementFaceGroup"

    def __init__(
        self, instance_to_wrap: "ListWithSelectedItem_CMSElementFaceGroup.TYPE"
    ):
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
    def implicit_type(cls) -> "_227.CMSElementFaceGroup.TYPE":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _227.CMSElementFaceGroup.TYPE

    @property
    def selected_value(self: Self) -> "_227.CMSElementFaceGroup":
        """mastapy.nodal_analysis.component_mode_synthesis.CMSElementFaceGroup

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[_227.CMSElementFaceGroup]":
        """List[mastapy.nodal_analysis.component_mode_synthesis.CMSElementFaceGroup]

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
