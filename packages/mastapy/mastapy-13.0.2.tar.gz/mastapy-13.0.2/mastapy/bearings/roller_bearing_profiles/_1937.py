"""RollerBearingConicalProfile"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_CONICAL_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingConicalProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingConicalProfile",)


Self = TypeVar("Self", bound="RollerBearingConicalProfile")


class RollerBearingConicalProfile(_1943.RollerBearingProfile):
    """RollerBearingConicalProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_CONICAL_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingConicalProfile")

    class _Cast_RollerBearingConicalProfile:
        """Special nested class for casting RollerBearingConicalProfile to subclasses."""

        def __init__(
            self: "RollerBearingConicalProfile._Cast_RollerBearingConicalProfile",
            parent: "RollerBearingConicalProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingConicalProfile._Cast_RollerBearingConicalProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_conical_profile(
            self: "RollerBearingConicalProfile._Cast_RollerBearingConicalProfile",
        ) -> "RollerBearingConicalProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingConicalProfile._Cast_RollerBearingConicalProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingConicalProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cone_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConeAngle

        if temp is None:
            return 0.0

        return temp

    @cone_angle.setter
    @enforce_parameter_types
    def cone_angle(self: Self, value: "float"):
        self.wrapped.ConeAngle = float(value) if value is not None else 0.0

    @property
    def deviation_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeviationOffset

        if temp is None:
            return 0.0

        return temp

    @deviation_offset.setter
    @enforce_parameter_types
    def deviation_offset(self: Self, value: "float"):
        self.wrapped.DeviationOffset = float(value) if value is not None else 0.0

    @property
    def deviation_at_end_of_component(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeviationAtEndOfComponent

        if temp is None:
            return 0.0

        return temp

    @deviation_at_end_of_component.setter
    @enforce_parameter_types
    def deviation_at_end_of_component(self: Self, value: "float"):
        self.wrapped.DeviationAtEndOfComponent = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingConicalProfile._Cast_RollerBearingConicalProfile":
        return self._Cast_RollerBearingConicalProfile(self)
