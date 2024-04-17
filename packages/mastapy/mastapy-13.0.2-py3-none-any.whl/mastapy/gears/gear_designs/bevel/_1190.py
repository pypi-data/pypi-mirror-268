"""DrivenMachineCharacteristicGleason"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DRIVEN_MACHINE_CHARACTERISTIC_GLEASON = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "DrivenMachineCharacteristicGleason"
)


__docformat__ = "restructuredtext en"
__all__ = ("DrivenMachineCharacteristicGleason",)


Self = TypeVar("Self", bound="DrivenMachineCharacteristicGleason")


class DrivenMachineCharacteristicGleason(Enum):
    """DrivenMachineCharacteristicGleason

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DRIVEN_MACHINE_CHARACTERISTIC_GLEASON

    UNIFORM = 0
    MEDIUM_SHOCK = 1
    HEAVY_SHOCK = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DrivenMachineCharacteristicGleason.__setattr__ = __enum_setattr
DrivenMachineCharacteristicGleason.__delattr__ = __enum_delattr
