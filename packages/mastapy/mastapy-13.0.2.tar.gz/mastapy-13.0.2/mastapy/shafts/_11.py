"""FkmMaterialGroup"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FKM_MATERIAL_GROUP = python_net_import("SMT.MastaAPI.Shafts", "FkmMaterialGroup")


__docformat__ = "restructuredtext en"
__all__ = ("FkmMaterialGroup",)


Self = TypeVar("Self", bound="FkmMaterialGroup")


class FkmMaterialGroup(Enum):
    """FkmMaterialGroup

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FKM_MATERIAL_GROUP

    CASE_HARDENING_STEEL = 0
    STAINLESS_STEEL = 1
    FORGING_STEEL = 2
    STEEL_OTHER_THAN_THESE = 3
    GS = 4
    GJS = 5
    GJM = 6
    GJL = 7
    WROUGHT_ALUMINIUM_ALLOYS = 8
    CAST_ALUMINIUM_ALLOYS = 9


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FkmMaterialGroup.__setattr__ = __enum_setattr
FkmMaterialGroup.__delattr__ = __enum_delattr
