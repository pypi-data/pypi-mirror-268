"""RollerBearingLundbergProfile"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_LUNDBERG_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingLundbergProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingLundbergProfile",)


Self = TypeVar("Self", bound="RollerBearingLundbergProfile")


class RollerBearingLundbergProfile(_1943.RollerBearingProfile):
    """RollerBearingLundbergProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_LUNDBERG_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingLundbergProfile")

    class _Cast_RollerBearingLundbergProfile:
        """Special nested class for casting RollerBearingLundbergProfile to subclasses."""

        def __init__(
            self: "RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile",
            parent: "RollerBearingLundbergProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_lundberg_profile(
            self: "RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile",
        ) -> "RollerBearingLundbergProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingLundbergProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Load

        if temp is None:
            return 0.0

        return temp

    @load.setter
    @enforce_parameter_types
    def load(self: Self, value: "float"):
        self.wrapped.Load = float(value) if value is not None else 0.0

    @property
    def use_bearing_dynamic_capacity(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseBearingDynamicCapacity

        if temp is None:
            return False

        return temp

    @use_bearing_dynamic_capacity.setter
    @enforce_parameter_types
    def use_bearing_dynamic_capacity(self: Self, value: "bool"):
        self.wrapped.UseBearingDynamicCapacity = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile":
        return self._Cast_RollerBearingLundbergProfile(self)
