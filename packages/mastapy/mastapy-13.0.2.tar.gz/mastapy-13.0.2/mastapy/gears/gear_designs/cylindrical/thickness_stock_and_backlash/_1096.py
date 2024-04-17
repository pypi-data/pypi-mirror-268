"""FinishStockType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FINISH_STOCK_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash",
    "FinishStockType",
)


__docformat__ = "restructuredtext en"
__all__ = ("FinishStockType",)


Self = TypeVar("Self", bound="FinishStockType")


class FinishStockType(Enum):
    """FinishStockType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FINISH_STOCK_TYPE

    NONE = 0
    SINGLE_VALUE = 1
    TOLERANCED_VALUE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FinishStockType.__setattr__ = __enum_setattr
FinishStockType.__delattr__ = __enum_delattr
