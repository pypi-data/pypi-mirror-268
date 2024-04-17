"""FileHistoryItem"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FILE_HISTORY_ITEM = python_net_import("SMT.MastaAPI.Utility", "FileHistoryItem")


__docformat__ = "restructuredtext en"
__all__ = ("FileHistoryItem",)


Self = TypeVar("Self", bound="FileHistoryItem")


class FileHistoryItem(_0.APIBase):
    """FileHistoryItem

    This is a mastapy class.
    """

    TYPE = _FILE_HISTORY_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FileHistoryItem")

    class _Cast_FileHistoryItem:
        """Special nested class for casting FileHistoryItem to subclasses."""

        def __init__(
            self: "FileHistoryItem._Cast_FileHistoryItem", parent: "FileHistoryItem"
        ):
            self._parent = parent

        @property
        def file_history_item(
            self: "FileHistoryItem._Cast_FileHistoryItem",
        ) -> "FileHistoryItem":
            return self._parent

        def __getattr__(self: "FileHistoryItem._Cast_FileHistoryItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FileHistoryItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @property
    def hash_code(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HashCode

        if temp is None:
            return ""

        return temp

    @property
    def licence_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LicenceID

        if temp is None:
            return ""

        return temp

    @property
    def save_date(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SaveDate

        if temp is None:
            return ""

        return temp

    @property
    def save_date_and_age(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SaveDateAndAge

        if temp is None:
            return ""

        return temp

    @property
    def user_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserName

        if temp is None:
            return ""

        return temp

    @property
    def version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Version

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "FileHistoryItem._Cast_FileHistoryItem":
        return self._Cast_FileHistoryItem(self)
