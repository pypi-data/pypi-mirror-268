"""SimpleTaskProgress"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "SimpleTaskProgress")


__docformat__ = "restructuredtext en"
__all__ = ("SimpleTaskProgress",)


Self = TypeVar("Self", bound="SimpleTaskProgress")


class SimpleTaskProgress(_7560.ConsoleProgress):
    """SimpleTaskProgress

    This is a mastapy class.
    """

    TYPE = _SIMPLE_TASK_PROGRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SimpleTaskProgress")

    class _Cast_SimpleTaskProgress:
        """Special nested class for casting SimpleTaskProgress to subclasses."""

        def __init__(
            self: "SimpleTaskProgress._Cast_SimpleTaskProgress",
            parent: "SimpleTaskProgress",
        ):
            self._parent = parent

        @property
        def simple_task_progress(
            self: "SimpleTaskProgress._Cast_SimpleTaskProgress",
        ) -> "SimpleTaskProgress":
            return self._parent

        def __getattr__(self: "SimpleTaskProgress._Cast_SimpleTaskProgress", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SimpleTaskProgress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def complete(self: Self):
        """Method does not return."""
        self.wrapped.Complete()

    @property
    def cast_to(self: Self) -> "SimpleTaskProgress._Cast_SimpleTaskProgress":
        return self._Cast_SimpleTaskProgress(self)
