"""CylindricalGearDesignAndRatingSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearDesignAndRatingSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignAndRatingSettings",)


Self = TypeVar("Self", bound="CylindricalGearDesignAndRatingSettings")


class CylindricalGearDesignAndRatingSettings(_0.APIBase):
    """CylindricalGearDesignAndRatingSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearDesignAndRatingSettings"
    )

    class _Cast_CylindricalGearDesignAndRatingSettings:
        """Special nested class for casting CylindricalGearDesignAndRatingSettings to subclasses."""

        def __init__(
            self: "CylindricalGearDesignAndRatingSettings._Cast_CylindricalGearDesignAndRatingSettings",
            parent: "CylindricalGearDesignAndRatingSettings",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_design_and_rating_settings(
            self: "CylindricalGearDesignAndRatingSettings._Cast_CylindricalGearDesignAndRatingSettings",
        ) -> "CylindricalGearDesignAndRatingSettings":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignAndRatingSettings._Cast_CylindricalGearDesignAndRatingSettings",
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
        self: Self, instance_to_wrap: "CylindricalGearDesignAndRatingSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDesignAndRatingSettings._Cast_CylindricalGearDesignAndRatingSettings":
        return self._Cast_CylindricalGearDesignAndRatingSettings(self)
