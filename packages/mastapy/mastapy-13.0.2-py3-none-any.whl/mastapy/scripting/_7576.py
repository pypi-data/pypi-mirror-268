"""ScriptingCommand"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _7561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTING_COMMAND = python_net_import(
    "SMT.MastaAPIUtility.Scripting", "ScriptingCommand"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScriptingCommand",)


Self = TypeVar("Self", bound="ScriptingCommand")


class ScriptingCommand(_7561.MarshalByRefObjectPermanent):
    """ScriptingCommand

    This is a mastapy class.
    """

    TYPE = _SCRIPTING_COMMAND
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScriptingCommand")

    class _Cast_ScriptingCommand:
        """Special nested class for casting ScriptingCommand to subclasses."""

        def __init__(
            self: "ScriptingCommand._Cast_ScriptingCommand", parent: "ScriptingCommand"
        ):
            self._parent = parent

        @property
        def scripting_command(
            self: "ScriptingCommand._Cast_ScriptingCommand",
        ) -> "ScriptingCommand":
            return self._parent

        def __getattr__(self: "ScriptingCommand._Cast_ScriptingCommand", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScriptingCommand.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def execute(self: Self):
        """Method does not return."""
        self.wrapped.Execute()

    @property
    def cast_to(self: Self) -> "ScriptingCommand._Cast_ScriptingCommand":
        return self._Cast_ScriptingCommand(self)
