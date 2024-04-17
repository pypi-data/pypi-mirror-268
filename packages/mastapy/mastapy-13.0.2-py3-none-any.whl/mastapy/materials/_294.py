"""WorkingCharacteristics"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_WORKING_CHARACTERISTICS = python_net_import(
    "SMT.MastaAPI.Materials", "WorkingCharacteristics"
)


__docformat__ = "restructuredtext en"
__all__ = ("WorkingCharacteristics",)


Self = TypeVar("Self", bound="WorkingCharacteristics")


class WorkingCharacteristics(Enum):
    """WorkingCharacteristics

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WORKING_CHARACTERISTICS

    UNIFORM = 0
    LIGHT_SHOCKS = 1
    MODERATE_SHOCKS = 2
    HEAVY_SHOCKS = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


WorkingCharacteristics.__setattr__ = __enum_setattr
WorkingCharacteristics.__delattr__ = __enum_delattr
