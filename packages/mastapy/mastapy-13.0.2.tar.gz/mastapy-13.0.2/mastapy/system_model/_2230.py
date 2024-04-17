"""ThermalExpansionOptionForGroundedNodes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_OPTION_FOR_GROUNDED_NODES = python_net_import(
    "SMT.MastaAPI.SystemModel", "ThermalExpansionOptionForGroundedNodes"
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermalExpansionOptionForGroundedNodes",)


Self = TypeVar("Self", bound="ThermalExpansionOptionForGroundedNodes")


class ThermalExpansionOptionForGroundedNodes(Enum):
    """ThermalExpansionOptionForGroundedNodes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _THERMAL_EXPANSION_OPTION_FOR_GROUNDED_NODES

    NO_EXPANSION = 0
    EXPAND_ALWAYS = 1
    EXPAND_IF_NO_GROUNDED_FE_SUBSTRUCTURES = 2
    EXPAND_IF_NO_FE_HOUSING = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ThermalExpansionOptionForGroundedNodes.__setattr__ = __enum_setattr
ThermalExpansionOptionForGroundedNodes.__delattr__ = __enum_delattr
