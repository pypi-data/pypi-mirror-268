"""CylindricalGearFlankRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFlankRating",)


Self = TypeVar("Self", bound="CylindricalGearFlankRating")


class CylindricalGearFlankRating(_362.GearFlankRating):
    """CylindricalGearFlankRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFlankRating")

    class _Cast_CylindricalGearFlankRating:
        """Special nested class for casting CylindricalGearFlankRating to subclasses."""

        def __init__(
            self: "CylindricalGearFlankRating._Cast_CylindricalGearFlankRating",
            parent: "CylindricalGearFlankRating",
        ):
            self._parent = parent

        @property
        def gear_flank_rating(
            self: "CylindricalGearFlankRating._Cast_CylindricalGearFlankRating",
        ) -> "_362.GearFlankRating":
            return self._parent._cast(_362.GearFlankRating)

        @property
        def cylindrical_gear_flank_rating(
            self: "CylindricalGearFlankRating._Cast_CylindricalGearFlankRating",
        ) -> "CylindricalGearFlankRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFlankRating._Cast_CylindricalGearFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worst_dynamic_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstDynamicFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_face_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstFaceLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFlankRating._Cast_CylindricalGearFlankRating":
        return self._Cast_CylindricalGearFlankRating(self)
