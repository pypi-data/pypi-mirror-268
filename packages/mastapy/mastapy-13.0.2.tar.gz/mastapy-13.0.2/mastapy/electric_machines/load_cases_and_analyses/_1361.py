"""ElectricMachineControlStrategy"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_CONTROL_STRATEGY = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineControlStrategy",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineControlStrategy",)


Self = TypeVar("Self", bound="ElectricMachineControlStrategy")


class ElectricMachineControlStrategy(Enum):
    """ElectricMachineControlStrategy

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_CONTROL_STRATEGY

    MAXIMUM_TORQUE_PER_AMPERE = 0
    MAXIMUM_EFFICIENCY = 1
    ID_0 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElectricMachineControlStrategy.__setattr__ = __enum_setattr
ElectricMachineControlStrategy.__delattr__ = __enum_delattr
