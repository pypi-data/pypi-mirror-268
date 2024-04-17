"""ElectricMachineSearchRegionSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_SEARCH_REGION_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel",
    "ElectricMachineSearchRegionSpecificationMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineSearchRegionSpecificationMethod",)


Self = TypeVar("Self", bound="ElectricMachineSearchRegionSpecificationMethod")


class ElectricMachineSearchRegionSpecificationMethod(Enum):
    """ElectricMachineSearchRegionSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_SEARCH_REGION_SPECIFICATION_METHOD

    FROM_POWER_LOAD = 0
    FROM_ELECTRIC_MACHINE_DETAIL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElectricMachineSearchRegionSpecificationMethod.__setattr__ = __enum_setattr
ElectricMachineSearchRegionSpecificationMethod.__delattr__ = __enum_delattr
