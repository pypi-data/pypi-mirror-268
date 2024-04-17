"""OilPumpDriveType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_OIL_PUMP_DRIVE_TYPE = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "OilPumpDriveType"
)


__docformat__ = "restructuredtext en"
__all__ = ("OilPumpDriveType",)


Self = TypeVar("Self", bound="OilPumpDriveType")


class OilPumpDriveType(Enum):
    """OilPumpDriveType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OIL_PUMP_DRIVE_TYPE

    MECHANICAL = 0
    ELECTRICAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


OilPumpDriveType.__setattr__ = __enum_setattr
OilPumpDriveType.__delattr__ = __enum_delattr
