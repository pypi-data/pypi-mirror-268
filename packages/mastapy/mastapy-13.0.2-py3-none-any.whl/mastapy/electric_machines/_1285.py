"""MagnetConfiguration"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MAGNET_CONFIGURATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "MagnetConfiguration"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagnetConfiguration",)


Self = TypeVar("Self", bound="MagnetConfiguration")


class MagnetConfiguration(Enum):
    """MagnetConfiguration

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MAGNET_CONFIGURATION

    NO_MAGNETS = 0
    INNER_MAGNETS_ONLY = 1
    OUTER_MAGNETS_ONLY = 2
    INNER_AND_OUTER_MAGNETS = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MagnetConfiguration.__setattr__ = __enum_setattr
MagnetConfiguration.__delattr__ = __enum_delattr
