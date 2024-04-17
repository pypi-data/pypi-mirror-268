"""ToothSlotStyle"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TOOTH_SLOT_STYLE = python_net_import("SMT.MastaAPI.ElectricMachines", "ToothSlotStyle")


__docformat__ = "restructuredtext en"
__all__ = ("ToothSlotStyle",)


Self = TypeVar("Self", bound="ToothSlotStyle")


class ToothSlotStyle(Enum):
    """ToothSlotStyle

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TOOTH_SLOT_STYLE

    PARALLEL_TOOTH = 0
    PARALLEL_SLOT = 1
    USERDEFINED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ToothSlotStyle.__setattr__ = __enum_setattr
ToothSlotStyle.__delattr__ = __enum_delattr
