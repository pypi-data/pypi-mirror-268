"""ShaftSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS = python_net_import("SMT.MastaAPI.Shafts", "ShaftSettings")


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSettings",)


Self = TypeVar("Self", bound="ShaftSettings")


class ShaftSettings(_0.APIBase):
    """ShaftSettings

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSettings")

    class _Cast_ShaftSettings:
        """Special nested class for casting ShaftSettings to subclasses."""

        def __init__(
            self: "ShaftSettings._Cast_ShaftSettings", parent: "ShaftSettings"
        ):
            self._parent = parent

        @property
        def shaft_settings(
            self: "ShaftSettings._Cast_ShaftSettings",
        ) -> "ShaftSettings":
            return self._parent

        def __getattr__(self: "ShaftSettings._Cast_ShaftSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSettings._Cast_ShaftSettings":
        return self._Cast_ShaftSettings(self)
