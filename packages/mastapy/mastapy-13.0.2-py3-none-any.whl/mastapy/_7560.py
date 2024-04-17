"""ConsoleProgress"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONSOLE_PROGRESS = python_net_import("SMT.MastaAPIUtility", "ConsoleProgress")


__docformat__ = "restructuredtext en"
__all__ = ("ConsoleProgress",)


Self = TypeVar("Self", bound="ConsoleProgress")


class ConsoleProgress(_7567.TaskProgress):
    """ConsoleProgress

    This is a mastapy class.
    """

    TYPE = _CONSOLE_PROGRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConsoleProgress")

    class _Cast_ConsoleProgress:
        """Special nested class for casting ConsoleProgress to subclasses."""

        def __init__(
            self: "ConsoleProgress._Cast_ConsoleProgress", parent: "ConsoleProgress"
        ):
            self._parent = parent

        @property
        def console_progress(
            self: "ConsoleProgress._Cast_ConsoleProgress",
        ) -> "ConsoleProgress":
            return self._parent

        def __getattr__(self: "ConsoleProgress._Cast_ConsoleProgress", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConsoleProgress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Id

        if temp is None:
            return 0

        return temp

    @enforce_parameter_types
    def add_error(self: Self, error: "str"):
        """Method does not return.

        Args:
            error (str)
        """
        error = str(error)
        self.wrapped.AddError(error if error else "")

    def complete(self: Self):
        """Method does not return."""
        self.wrapped.Complete()

    @property
    def cast_to(self: Self) -> "ConsoleProgress._Cast_ConsoleProgress":
        return self._Cast_ConsoleProgress(self)
