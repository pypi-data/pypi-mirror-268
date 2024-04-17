"""ElectricMachineForceViewOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FORCE_VIEW_OPTIONS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineForceViewOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineForceViewOptions",)


Self = TypeVar("Self", bound="ElectricMachineForceViewOptions")


class ElectricMachineForceViewOptions(Enum):
    """ElectricMachineForceViewOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_FORCE_VIEW_OPTIONS

    NONE = 0
    AIR_GAP_FORCE_DENSITY_ON_STATOR = 1
    STATOR_TOOTH_RESULTANT_FORCES = 2
    STATOR_TOOTH_RADIAL_FORCES = 3
    STATOR_TOOTH_TANGENTIAL_FORCES = 4
    STATOR_TOOTH_RADIAL_AND_TANGENTIAL_FORCES = 5
    STATOR_TOOTH_AXIAL_MOMENTS = 6
    STATOR_TOOTH_FORCE_DENSITY_AND_AXIAL_MOMENTS = 7


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElectricMachineForceViewOptions.__setattr__ = __enum_setattr
ElectricMachineForceViewOptions.__delattr__ = __enum_delattr
