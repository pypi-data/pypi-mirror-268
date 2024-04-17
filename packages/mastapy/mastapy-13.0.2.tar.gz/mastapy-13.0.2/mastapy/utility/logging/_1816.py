"""Message"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESSAGE = python_net_import("SMT.MastaAPI.Utility.Logging", "Message")


__docformat__ = "restructuredtext en"
__all__ = ("Message",)


Self = TypeVar("Self", bound="Message")


class Message(_0.APIBase):
    """Message

    This is a mastapy class.
    """

    TYPE = _MESSAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Message")

    class _Cast_Message:
        """Special nested class for casting Message to subclasses."""

        def __init__(self: "Message._Cast_Message", parent: "Message"):
            self._parent = parent

        @property
        def message(self: "Message._Cast_Message") -> "Message":
            return self._parent

        def __getattr__(self: "Message._Cast_Message", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Message.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def text(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Text

        if temp is None:
            return ""

        return temp

    @property
    def verbose(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Verbose

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self: Self) -> "Message._Cast_Message":
        return self._Cast_Message(self)
