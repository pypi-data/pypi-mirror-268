"""ActiveConicalFlank"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ACTIVE_CONICAL_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ActiveConicalFlank"
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveConicalFlank",)


Self = TypeVar("Self", bound="ActiveConicalFlank")


class ActiveConicalFlank(Enum):
    """ActiveConicalFlank

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ACTIVE_CONICAL_FLANK

    DRIVE = 0
    COAST = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ActiveConicalFlank.__setattr__ = __enum_setattr
ActiveConicalFlank.__delattr__ = __enum_delattr
