"""DatabaseWithSelectedItem"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("DatabaseWithSelectedItem",)


Self = TypeVar("Self", bound="DatabaseWithSelectedItem")


class DatabaseWithSelectedItem(_0.APIBase):
    """DatabaseWithSelectedItem

    This is a mastapy class.
    """

    TYPE = _DATABASE_WITH_SELECTED_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatabaseWithSelectedItem")

    class _Cast_DatabaseWithSelectedItem:
        """Special nested class for casting DatabaseWithSelectedItem to subclasses."""

        def __init__(
            self: "DatabaseWithSelectedItem._Cast_DatabaseWithSelectedItem",
            parent: "DatabaseWithSelectedItem",
        ):
            self._parent = parent

        @property
        def database_with_selected_item(
            self: "DatabaseWithSelectedItem._Cast_DatabaseWithSelectedItem",
        ) -> "DatabaseWithSelectedItem":
            return self._parent

        def __getattr__(
            self: "DatabaseWithSelectedItem._Cast_DatabaseWithSelectedItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatabaseWithSelectedItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def selected_item_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedItemName

        if temp is None:
            return ""

        return temp

    @enforce_parameter_types
    def set_selected_item(self: Self, item_name: "str"):
        """Method does not return.

        Args:
            item_name (str)
        """
        item_name = str(item_name)
        self.wrapped.SetSelectedItem(item_name if item_name else "")

    @property
    def cast_to(
        self: Self,
    ) -> "DatabaseWithSelectedItem._Cast_DatabaseWithSelectedItem":
        return self._Cast_DatabaseWithSelectedItem(self)
