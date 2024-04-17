"""ColumnTitle"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_TITLE = python_net_import(
    "SMT.MastaAPI.Utility.FileAccessHelpers", "ColumnTitle"
)


__docformat__ = "restructuredtext en"
__all__ = ("ColumnTitle",)


Self = TypeVar("Self", bound="ColumnTitle")


class ColumnTitle(_0.APIBase):
    """ColumnTitle

    This is a mastapy class.
    """

    TYPE = _COLUMN_TITLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ColumnTitle")

    class _Cast_ColumnTitle:
        """Special nested class for casting ColumnTitle to subclasses."""

        def __init__(self: "ColumnTitle._Cast_ColumnTitle", parent: "ColumnTitle"):
            self._parent = parent

        @property
        def column_title(self: "ColumnTitle._Cast_ColumnTitle") -> "ColumnTitle":
            return self._parent

        def __getattr__(self: "ColumnTitle._Cast_ColumnTitle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ColumnTitle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column_number(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ColumnNumber

        if temp is None:
            return 0

        return temp

    @property
    def title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Title

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "ColumnTitle._Cast_ColumnTitle":
        return self._Cast_ColumnTitle(self)
