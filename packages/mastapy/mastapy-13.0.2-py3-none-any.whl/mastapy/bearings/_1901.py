"""RollingBearingKey"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_KEY = python_net_import("SMT.MastaAPI.Bearings", "RollingBearingKey")


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingKey",)


Self = TypeVar("Self", bound="RollingBearingKey")


class RollingBearingKey(_1833.DatabaseKey):
    """RollingBearingKey

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingKey")

    class _Cast_RollingBearingKey:
        """Special nested class for casting RollingBearingKey to subclasses."""

        def __init__(
            self: "RollingBearingKey._Cast_RollingBearingKey",
            parent: "RollingBearingKey",
        ):
            self._parent = parent

        @property
        def database_key(
            self: "RollingBearingKey._Cast_RollingBearingKey",
        ) -> "_1833.DatabaseKey":
            return self._parent._cast(_1833.DatabaseKey)

        @property
        def rolling_bearing_key(
            self: "RollingBearingKey._Cast_RollingBearingKey",
        ) -> "RollingBearingKey":
            return self._parent

        def __getattr__(self: "RollingBearingKey._Cast_RollingBearingKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearingKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RollingBearingKey._Cast_RollingBearingKey":
        return self._Cast_RollingBearingKey(self)
