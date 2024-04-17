"""ProfileDataToUse"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PROFILE_DATA_TO_USE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "ProfileDataToUse"
)


__docformat__ = "restructuredtext en"
__all__ = ("ProfileDataToUse",)


Self = TypeVar("Self", bound="ProfileDataToUse")


class ProfileDataToUse(Enum):
    """ProfileDataToUse

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PROFILE_DATA_TO_USE

    ACTUAL_DATA = 0
    SMOOTHED = 1
    FITTED_STANDARD_PROFILE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ProfileDataToUse.__setattr__ = __enum_setattr
ProfileDataToUse.__delattr__ = __enum_delattr
