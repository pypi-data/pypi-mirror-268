"""AirGapPartition"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AIR_GAP_PARTITION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "AirGapPartition"
)


__docformat__ = "restructuredtext en"
__all__ = ("AirGapPartition",)


Self = TypeVar("Self", bound="AirGapPartition")


class AirGapPartition(Enum):
    """AirGapPartition

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AIR_GAP_PARTITION

    MIDDLE = 0
    OFFSET = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AirGapPartition.__setattr__ = __enum_setattr
AirGapPartition.__delattr__ = __enum_delattr
