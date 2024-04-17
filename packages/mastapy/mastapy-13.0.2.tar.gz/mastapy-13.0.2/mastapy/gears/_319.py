"""BevelHypoidGearDesignSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears", "BevelHypoidGearDesignSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearDesignSettings",)


Self = TypeVar("Self", bound="BevelHypoidGearDesignSettings")


class BevelHypoidGearDesignSettings(_0.APIBase):
    """BevelHypoidGearDesignSettings

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelHypoidGearDesignSettings")

    class _Cast_BevelHypoidGearDesignSettings:
        """Special nested class for casting BevelHypoidGearDesignSettings to subclasses."""

        def __init__(
            self: "BevelHypoidGearDesignSettings._Cast_BevelHypoidGearDesignSettings",
            parent: "BevelHypoidGearDesignSettings",
        ):
            self._parent = parent

        @property
        def bevel_hypoid_gear_design_settings(
            self: "BevelHypoidGearDesignSettings._Cast_BevelHypoidGearDesignSettings",
        ) -> "BevelHypoidGearDesignSettings":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearDesignSettings._Cast_BevelHypoidGearDesignSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelHypoidGearDesignSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearDesignSettings._Cast_BevelHypoidGearDesignSettings":
        return self._Cast_BevelHypoidGearDesignSettings(self)
