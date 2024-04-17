"""MachineCharacteristicAGMAKlingelnberg"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MACHINE_CHARACTERISTIC_AGMA_KLINGELNBERG = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "MachineCharacteristicAGMAKlingelnberg"
)


__docformat__ = "restructuredtext en"
__all__ = ("MachineCharacteristicAGMAKlingelnberg",)


Self = TypeVar("Self", bound="MachineCharacteristicAGMAKlingelnberg")


class MachineCharacteristicAGMAKlingelnberg(Enum):
    """MachineCharacteristicAGMAKlingelnberg

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MACHINE_CHARACTERISTIC_AGMA_KLINGELNBERG

    UNIFORM = 0
    LIGHT_SHOCK = 1
    MEDIUM_SHOCK = 2
    HEAVY_SHOCK = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MachineCharacteristicAGMAKlingelnberg.__setattr__ = __enum_setattr
MachineCharacteristicAGMAKlingelnberg.__delattr__ = __enum_delattr
