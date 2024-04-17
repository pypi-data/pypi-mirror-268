"""ElectricMachineType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_TYPE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineType",)


Self = TypeVar("Self", bound="ElectricMachineType")


class ElectricMachineType(Enum):
    """ElectricMachineType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_TYPE

    INTERIOR_PERMANENT_MAGNET = 0
    PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE = 1
    SYNCHRONOUS_RELUCTANCE = 2
    SURFACE_PERMANENT_MAGNET = 3
    WOUND_FIELD_SYNCHRONOUS = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElectricMachineType.__setattr__ = __enum_setattr
ElectricMachineType.__delattr__ = __enum_delattr
