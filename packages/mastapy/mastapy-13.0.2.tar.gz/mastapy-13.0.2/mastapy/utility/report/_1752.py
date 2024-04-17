"""CadPageOrientation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CAD_PAGE_ORIENTATION = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CadPageOrientation"
)


__docformat__ = "restructuredtext en"
__all__ = ("CadPageOrientation",)


Self = TypeVar("Self", bound="CadPageOrientation")


class CadPageOrientation(Enum):
    """CadPageOrientation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CAD_PAGE_ORIENTATION

    LANDSCAPE = 0
    PORTRAIT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CadPageOrientation.__setattr__ = __enum_setattr
CadPageOrientation.__delattr__ = __enum_delattr
