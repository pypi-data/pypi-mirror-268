"""BevelHypoidGearRatingSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears", "BevelHypoidGearRatingSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearRatingSettings",)


Self = TypeVar("Self", bound="BevelHypoidGearRatingSettings")


class BevelHypoidGearRatingSettings(_0.APIBase):
    """BevelHypoidGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelHypoidGearRatingSettings")

    class _Cast_BevelHypoidGearRatingSettings:
        """Special nested class for casting BevelHypoidGearRatingSettings to subclasses."""

        def __init__(
            self: "BevelHypoidGearRatingSettings._Cast_BevelHypoidGearRatingSettings",
            parent: "BevelHypoidGearRatingSettings",
        ):
            self._parent = parent

        @property
        def bevel_hypoid_gear_rating_settings(
            self: "BevelHypoidGearRatingSettings._Cast_BevelHypoidGearRatingSettings",
        ) -> "BevelHypoidGearRatingSettings":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearRatingSettings._Cast_BevelHypoidGearRatingSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelHypoidGearRatingSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearRatingSettings._Cast_BevelHypoidGearRatingSettings":
        return self._Cast_BevelHypoidGearRatingSettings(self)
