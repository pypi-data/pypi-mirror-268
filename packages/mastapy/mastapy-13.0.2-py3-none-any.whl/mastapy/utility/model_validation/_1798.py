"""Fix"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FIX = python_net_import("SMT.MastaAPI.Utility.ModelValidation", "Fix")


__docformat__ = "restructuredtext en"
__all__ = ("Fix",)


Self = TypeVar("Self", bound="Fix")


class Fix(_0.APIBase):
    """Fix

    This is a mastapy class.
    """

    TYPE = _FIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Fix")

    class _Cast_Fix:
        """Special nested class for casting Fix to subclasses."""

        def __init__(self: "Fix._Cast_Fix", parent: "Fix"):
            self._parent = parent

        @property
        def fix(self: "Fix._Cast_Fix") -> "Fix":
            return self._parent

        def __getattr__(self: "Fix._Cast_Fix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Fix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Description

        if temp is None:
            return ""

        return temp

    def perform(self: Self):
        """Method does not return."""
        self.wrapped.Perform()

    @property
    def cast_to(self: Self) -> "Fix._Cast_Fix":
        return self._Cast_Fix(self)
