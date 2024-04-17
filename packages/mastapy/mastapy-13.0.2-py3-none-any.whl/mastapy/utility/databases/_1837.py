"""NamedKey"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_KEY = python_net_import("SMT.MastaAPI.Utility.Databases", "NamedKey")


__docformat__ = "restructuredtext en"
__all__ = ("NamedKey",)


Self = TypeVar("Self", bound="NamedKey")


class NamedKey(_1833.DatabaseKey):
    """NamedKey

    This is a mastapy class.
    """

    TYPE = _NAMED_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedKey")

    class _Cast_NamedKey:
        """Special nested class for casting NamedKey to subclasses."""

        def __init__(self: "NamedKey._Cast_NamedKey", parent: "NamedKey"):
            self._parent = parent

        @property
        def database_key(self: "NamedKey._Cast_NamedKey") -> "_1833.DatabaseKey":
            return self._parent._cast(_1833.DatabaseKey)

        @property
        def named_key(self: "NamedKey._Cast_NamedKey") -> "NamedKey":
            return self._parent

        def __getattr__(self: "NamedKey._Cast_NamedKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def cast_to(self: Self) -> "NamedKey._Cast_NamedKey":
        return self._Cast_NamedKey(self)
