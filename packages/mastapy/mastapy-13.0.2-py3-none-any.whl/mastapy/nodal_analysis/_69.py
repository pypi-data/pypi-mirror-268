"""GearMeshContactStatus"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_MESH_CONTACT_STATUS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "GearMeshContactStatus"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshContactStatus",)


Self = TypeVar("Self", bound="GearMeshContactStatus")


class GearMeshContactStatus(Enum):
    """GearMeshContactStatus

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_MESH_CONTACT_STATUS

    NO_CONTACT = 0
    LEFT_FLANK = 1
    BOTH_FLANKS = 2
    RIGHT_FLANK = -1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearMeshContactStatus.__setattr__ = __enum_setattr
GearMeshContactStatus.__delattr__ = __enum_delattr
