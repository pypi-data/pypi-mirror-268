"""RollerBearingFlatProfile"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.roller_bearing_profiles import _1943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_FLAT_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingFlatProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingFlatProfile",)


Self = TypeVar("Self", bound="RollerBearingFlatProfile")


class RollerBearingFlatProfile(_1943.RollerBearingProfile):
    """RollerBearingFlatProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_FLAT_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingFlatProfile")

    class _Cast_RollerBearingFlatProfile:
        """Special nested class for casting RollerBearingFlatProfile to subclasses."""

        def __init__(
            self: "RollerBearingFlatProfile._Cast_RollerBearingFlatProfile",
            parent: "RollerBearingFlatProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_profile(
            self: "RollerBearingFlatProfile._Cast_RollerBearingFlatProfile",
        ) -> "_1943.RollerBearingProfile":
            return self._parent._cast(_1943.RollerBearingProfile)

        @property
        def roller_bearing_flat_profile(
            self: "RollerBearingFlatProfile._Cast_RollerBearingFlatProfile",
        ) -> "RollerBearingFlatProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingFlatProfile._Cast_RollerBearingFlatProfile", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingFlatProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RollerBearingFlatProfile._Cast_RollerBearingFlatProfile":
        return self._Cast_RollerBearingFlatProfile(self)
