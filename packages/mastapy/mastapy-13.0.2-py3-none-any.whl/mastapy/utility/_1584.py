"""Command"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _7561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMMAND = python_net_import("SMT.MastaAPI.Utility", "Command")


__docformat__ = "restructuredtext en"
__all__ = ("Command",)


Self = TypeVar("Self", bound="Command")


class Command(_7561.MarshalByRefObjectPermanent):
    """Command

    This is a mastapy class.
    """

    TYPE = _COMMAND
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Command")

    class _Cast_Command:
        """Special nested class for casting Command to subclasses."""

        def __init__(self: "Command._Cast_Command", parent: "Command"):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "Command._Cast_Command",
        ) -> "_7561.MarshalByRefObjectPermanent":
            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def command(self: "Command._Cast_Command") -> "Command":
            return self._parent

        def __getattr__(self: "Command._Cast_Command", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Command.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def run(self: Self):
        """Method does not return."""
        self.wrapped.Run()

    @property
    def cast_to(self: Self) -> "Command._Cast_Command":
        return self._Cast_Command(self)
