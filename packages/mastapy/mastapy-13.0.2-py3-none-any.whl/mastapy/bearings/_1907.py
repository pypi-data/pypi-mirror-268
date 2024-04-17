"""TiltingPadTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TILTING_PAD_TYPES = python_net_import("SMT.MastaAPI.Bearings", "TiltingPadTypes")


__docformat__ = "restructuredtext en"
__all__ = ("TiltingPadTypes",)


Self = TypeVar("Self", bound="TiltingPadTypes")


class TiltingPadTypes(Enum):
    """TiltingPadTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TILTING_PAD_TYPES

    NONEQUALISED = 0
    EQUALISED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TiltingPadTypes.__setattr__ = __enum_setattr
TiltingPadTypes.__delattr__ = __enum_delattr
