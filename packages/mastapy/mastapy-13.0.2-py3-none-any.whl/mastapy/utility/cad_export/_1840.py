"""StockDrawings"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_STOCK_DRAWINGS = python_net_import("SMT.MastaAPI.Utility.CadExport", "StockDrawings")


__docformat__ = "restructuredtext en"
__all__ = ("StockDrawings",)


Self = TypeVar("Self", bound="StockDrawings")


class StockDrawings(Enum):
    """StockDrawings

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _STOCK_DRAWINGS

    GEAR_CHAMFER_DETAIL = 0
    RACK_WITH_SEMI_TOPPING = 1
    RACK_WITHOUT_SEMI_TOPPING = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


StockDrawings.__setattr__ = __enum_setattr
StockDrawings.__delattr__ = __enum_delattr
