"""Eigenmode"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EIGENMODE = python_net_import("SMT.MastaAPI.MathUtility", "Eigenmode")


__docformat__ = "restructuredtext en"
__all__ = ("Eigenmode",)


Self = TypeVar("Self", bound="Eigenmode")


class Eigenmode(_0.APIBase):
    """Eigenmode

    This is a mastapy class.
    """

    TYPE = _EIGENMODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Eigenmode")

    class _Cast_Eigenmode:
        """Special nested class for casting Eigenmode to subclasses."""

        def __init__(self: "Eigenmode._Cast_Eigenmode", parent: "Eigenmode"):
            self._parent = parent

        @property
        def eigenmode(self: "Eigenmode._Cast_Eigenmode") -> "Eigenmode":
            return self._parent

        def __getattr__(self: "Eigenmode._Cast_Eigenmode", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Eigenmode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "Eigenmode._Cast_Eigenmode":
        return self._Cast_Eigenmode(self)
