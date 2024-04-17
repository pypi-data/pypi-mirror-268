"""MKLVersion"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MKL_VERSION = python_net_import("SMT.MastaAPI.Utility", "MKLVersion")


__docformat__ = "restructuredtext en"
__all__ = ("MKLVersion",)


Self = TypeVar("Self", bound="MKLVersion")


class MKLVersion(_0.APIBase):
    """MKLVersion

    This is a mastapy class.
    """

    TYPE = _MKL_VERSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MKLVersion")

    class _Cast_MKLVersion:
        """Special nested class for casting MKLVersion to subclasses."""

        def __init__(self: "MKLVersion._Cast_MKLVersion", parent: "MKLVersion"):
            self._parent = parent

        @property
        def mkl_version(self: "MKLVersion._Cast_MKLVersion") -> "MKLVersion":
            return self._parent

        def __getattr__(self: "MKLVersion._Cast_MKLVersion", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MKLVersion.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def build(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Build

        if temp is None:
            return ""

        return temp

    @property
    def instruction_set(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InstructionSet

        if temp is None:
            return ""

        return temp

    @property
    def platform(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Platform

        if temp is None:
            return ""

        return temp

    @property
    def processor(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Processor

        if temp is None:
            return ""

        return temp

    @property
    def product_status(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProductStatus

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
    def cast_to(self: Self) -> "MKLVersion._Cast_MKLVersion":
        return self._Cast_MKLVersion(self)
