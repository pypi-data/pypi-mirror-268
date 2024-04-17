"""ScriptingExecutionCommand"""

from __future__ import annotations

from typing import TypeVar

from mastapy.scripting import _7576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTING_EXECUTION_COMMAND = python_net_import(
    "SMT.MastaAPIUtility.Scripting", "ScriptingExecutionCommand"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScriptingExecutionCommand",)


Self = TypeVar("Self", bound="ScriptingExecutionCommand")


class ScriptingExecutionCommand(_7576.ScriptingCommand):
    """ScriptingExecutionCommand

    This is a mastapy class.
    """

    TYPE = _SCRIPTING_EXECUTION_COMMAND
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScriptingExecutionCommand")

    class _Cast_ScriptingExecutionCommand:
        """Special nested class for casting ScriptingExecutionCommand to subclasses."""

        def __init__(
            self: "ScriptingExecutionCommand._Cast_ScriptingExecutionCommand",
            parent: "ScriptingExecutionCommand",
        ):
            self._parent = parent

        @property
        def scripting_execution_command(
            self: "ScriptingExecutionCommand._Cast_ScriptingExecutionCommand",
        ) -> "ScriptingExecutionCommand":
            return self._parent

        def __getattr__(
            self: "ScriptingExecutionCommand._Cast_ScriptingExecutionCommand", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScriptingExecutionCommand.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def execute(self: Self):
        """Method does not return."""
        self.wrapped.Execute()

    @property
    def cast_to(
        self: Self,
    ) -> "ScriptingExecutionCommand._Cast_ScriptingExecutionCommand":
        return self._Cast_ScriptingExecutionCommand(self)
