"""Table4JointInterfaceTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TABLE_4_JOINT_INTERFACE_TYPES = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "Table4JointInterfaceTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("Table4JointInterfaceTypes",)


Self = TypeVar("Self", bound="Table4JointInterfaceTypes")


class Table4JointInterfaceTypes(Enum):
    """Table4JointInterfaceTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TABLE_4_JOINT_INTERFACE_TYPES

    STEELSTEEL_INTERFACE_JOINED_WITH_MINERAL_OIL = 0
    STEELSTEEL_INTERFACE_JOINED_WITH_OIL_AND_DEGREASED_SURFACES_GLYCERINE = 1
    STEELSTEEL_INTERFACE_JOINED_WITH_THERMAL_EXPANSION = 2
    STEELSTEEL_INTERFACE_JOINED_WITH_THERMAL_EXPANSION_AND_DEGREASED_SURFACES = 3
    STEELIRON_INTERFACE_JOINED_WITH_MINERAL_OIL = 4
    STEELIRON_INTERFACE_JOINED_WITH_OIL_AND_DEGREASED_SURFACES = 5
    STEELMGAL_INTERFACE_DRY = 6
    STEELCUZN_INTERFACE_DRY = 7


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


Table4JointInterfaceTypes.__setattr__ = __enum_setattr
Table4JointInterfaceTypes.__delattr__ = __enum_delattr
