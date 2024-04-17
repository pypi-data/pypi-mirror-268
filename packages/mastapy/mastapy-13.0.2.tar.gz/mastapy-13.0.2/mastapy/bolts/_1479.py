"""BoltSection"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_SECTION = python_net_import("SMT.MastaAPI.Bolts", "BoltSection")


__docformat__ = "restructuredtext en"
__all__ = ("BoltSection",)


Self = TypeVar("Self", bound="BoltSection")


class BoltSection(_0.APIBase):
    """BoltSection

    This is a mastapy class.
    """

    TYPE = _BOLT_SECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltSection")

    class _Cast_BoltSection:
        """Special nested class for casting BoltSection to subclasses."""

        def __init__(self: "BoltSection._Cast_BoltSection", parent: "BoltSection"):
            self._parent = parent

        @property
        def bolt_section(self: "BoltSection._Cast_BoltSection") -> "BoltSection":
            return self._parent

        def __getattr__(self: "BoltSection._Cast_BoltSection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltSection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def inner_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @inner_diameter.setter
    @enforce_parameter_types
    def inner_diameter(self: Self, value: "float"):
        self.wrapped.InnerDiameter = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "BoltSection._Cast_BoltSection":
        return self._Cast_BoltSection(self)
