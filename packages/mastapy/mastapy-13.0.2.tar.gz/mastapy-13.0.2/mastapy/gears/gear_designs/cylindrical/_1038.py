"""CylindricalGearTableMGItemDetail"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TABLE_MG_ITEM_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearTableMGItemDetail"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTableMGItemDetail",)


Self = TypeVar("Self", bound="CylindricalGearTableMGItemDetail")


class CylindricalGearTableMGItemDetail(Enum):
    """CylindricalGearTableMGItemDetail

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_GEAR_TABLE_MG_ITEM_DETAIL

    CHART = 0
    REPORT = 1
    REPORT_AND_CHART = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalGearTableMGItemDetail.__setattr__ = __enum_setattr
CylindricalGearTableMGItemDetail.__delattr__ = __enum_delattr
