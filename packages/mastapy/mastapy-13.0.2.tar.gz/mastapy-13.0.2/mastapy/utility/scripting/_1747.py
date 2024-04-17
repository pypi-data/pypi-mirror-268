"""UserDefinedPropertyKey"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_DEFINED_PROPERTY_KEY = python_net_import(
    "SMT.MastaAPI.Utility.Scripting", "UserDefinedPropertyKey"
)


__docformat__ = "restructuredtext en"
__all__ = ("UserDefinedPropertyKey",)


Self = TypeVar("Self", bound="UserDefinedPropertyKey")


class UserDefinedPropertyKey(_1833.DatabaseKey):
    """UserDefinedPropertyKey

    This is a mastapy class.
    """

    TYPE = _USER_DEFINED_PROPERTY_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UserDefinedPropertyKey")

    class _Cast_UserDefinedPropertyKey:
        """Special nested class for casting UserDefinedPropertyKey to subclasses."""

        def __init__(
            self: "UserDefinedPropertyKey._Cast_UserDefinedPropertyKey",
            parent: "UserDefinedPropertyKey",
        ):
            self._parent = parent

        @property
        def database_key(
            self: "UserDefinedPropertyKey._Cast_UserDefinedPropertyKey",
        ) -> "_1833.DatabaseKey":
            return self._parent._cast(_1833.DatabaseKey)

        @property
        def user_defined_property_key(
            self: "UserDefinedPropertyKey._Cast_UserDefinedPropertyKey",
        ) -> "UserDefinedPropertyKey":
            return self._parent

        def __getattr__(
            self: "UserDefinedPropertyKey._Cast_UserDefinedPropertyKey", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UserDefinedPropertyKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "UserDefinedPropertyKey._Cast_UserDefinedPropertyKey":
        return self._Cast_UserDefinedPropertyKey(self)
