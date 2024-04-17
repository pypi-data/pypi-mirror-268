"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
from mastapy._internal import constructor, conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_AbstractPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ListWithSelectedItem_AbstractPeriodicExcitationDetail")


class ListWithSelectedItem_AbstractPeriodicExcitationDetail(
    _5687.AbstractPeriodicExcitationDetail, mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_AbstractPeriodicExcitationDetail

    A specific implementation of 'ListWithSelectedItem' for 'AbstractPeriodicExcitationDetail' types.
    """

    __qualname__ = "AbstractPeriodicExcitationDetail"

    def __init__(
        self,
        instance_to_wrap: "ListWithSelectedItem_AbstractPeriodicExcitationDetail.TYPE",
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
    def implicit_type(cls) -> "_5687.AbstractPeriodicExcitationDetail.TYPE":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5687.AbstractPeriodicExcitationDetail.TYPE

    @property
    def selected_value(self: Self) -> "_5687.AbstractPeriodicExcitationDetail":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractPeriodicExcitationDetail

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[_5687.AbstractPeriodicExcitationDetail]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractPeriodicExcitationDetail]

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
