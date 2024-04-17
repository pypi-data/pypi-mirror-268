"""CylindricalMftRoughingMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MFT_ROUGHING_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalMftRoughingMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMftRoughingMethods",)


Self = TypeVar("Self", bound="CylindricalMftRoughingMethods")


class CylindricalMftRoughingMethods(Enum):
    """CylindricalMftRoughingMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_MFT_ROUGHING_METHODS

    HOBBING = 0
    SHAPING = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalMftRoughingMethods.__setattr__ = __enum_setattr
CylindricalMftRoughingMethods.__delattr__ = __enum_delattr
