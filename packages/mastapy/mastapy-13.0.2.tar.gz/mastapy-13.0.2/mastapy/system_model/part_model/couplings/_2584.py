"""BeltDriveType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDriveType"
)


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveType",)


Self = TypeVar("Self", bound="BeltDriveType")


class BeltDriveType(Enum):
    """BeltDriveType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BELT_DRIVE_TYPE

    PUSHBELT = 0
    PULLBELT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BeltDriveType.__setattr__ = __enum_setattr
BeltDriveType.__delattr__ = __enum_delattr
