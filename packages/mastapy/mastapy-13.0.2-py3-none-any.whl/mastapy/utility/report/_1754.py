"""CadTableBorderType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CAD_TABLE_BORDER_TYPE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CadTableBorderType"
)


__docformat__ = "restructuredtext en"
__all__ = ("CadTableBorderType",)


Self = TypeVar("Self", bound="CadTableBorderType")


class CadTableBorderType(Enum):
    """CadTableBorderType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CAD_TABLE_BORDER_TYPE

    SINGLE = 0
    DOUBLE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CadTableBorderType.__setattr__ = __enum_setattr
CadTableBorderType.__delattr__ = __enum_delattr
