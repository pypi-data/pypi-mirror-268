"""CylindricalPlasticGearRatingSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalPlasticGearRatingSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlasticGearRatingSettings",)


Self = TypeVar("Self", bound="CylindricalPlasticGearRatingSettings")


class CylindricalPlasticGearRatingSettings(_0.APIBase):
    """CylindricalPlasticGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlasticGearRatingSettings")

    class _Cast_CylindricalPlasticGearRatingSettings:
        """Special nested class for casting CylindricalPlasticGearRatingSettings to subclasses."""

        def __init__(
            self: "CylindricalPlasticGearRatingSettings._Cast_CylindricalPlasticGearRatingSettings",
            parent: "CylindricalPlasticGearRatingSettings",
        ):
            self._parent = parent

        @property
        def cylindrical_plastic_gear_rating_settings(
            self: "CylindricalPlasticGearRatingSettings._Cast_CylindricalPlasticGearRatingSettings",
        ) -> "CylindricalPlasticGearRatingSettings":
            return self._parent

        def __getattr__(
            self: "CylindricalPlasticGearRatingSettings._Cast_CylindricalPlasticGearRatingSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalPlasticGearRatingSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlasticGearRatingSettings._Cast_CylindricalPlasticGearRatingSettings":
        return self._Cast_CylindricalPlasticGearRatingSettings(self)
