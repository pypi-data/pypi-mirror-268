"""CylindricalGearSpecifiedProfile"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFIED_PROFILE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalGearSpecifiedProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSpecifiedProfile",)


Self = TypeVar("Self", bound="CylindricalGearSpecifiedProfile")


class CylindricalGearSpecifiedProfile(_0.APIBase):
    """CylindricalGearSpecifiedProfile

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SPECIFIED_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSpecifiedProfile")

    class _Cast_CylindricalGearSpecifiedProfile:
        """Special nested class for casting CylindricalGearSpecifiedProfile to subclasses."""

        def __init__(
            self: "CylindricalGearSpecifiedProfile._Cast_CylindricalGearSpecifiedProfile",
            parent: "CylindricalGearSpecifiedProfile",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_specified_profile(
            self: "CylindricalGearSpecifiedProfile._Cast_CylindricalGearSpecifiedProfile",
        ) -> "CylindricalGearSpecifiedProfile":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSpecifiedProfile._Cast_CylindricalGearSpecifiedProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSpecifiedProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_at_minimum_roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OffsetAtMinimumRollDistance

        if temp is None:
            return 0.0

        return temp

    @offset_at_minimum_roll_distance.setter
    @enforce_parameter_types
    def offset_at_minimum_roll_distance(self: Self, value: "float"):
        self.wrapped.OffsetAtMinimumRollDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSpecifiedProfile._Cast_CylindricalGearSpecifiedProfile":
        return self._Cast_CylindricalGearSpecifiedProfile(self)
