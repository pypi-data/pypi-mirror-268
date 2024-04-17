"""LubricantDefinition"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LUBRICANT_DEFINITION = python_net_import(
    "SMT.MastaAPI.Materials", "LubricantDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("LubricantDefinition",)


Self = TypeVar("Self", bound="LubricantDefinition")


class LubricantDefinition(Enum):
    """LubricantDefinition

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LUBRICANT_DEFINITION

    STANDARD = 0
    AGMA_925A03 = 1
    VDI_27362014 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LubricantDefinition.__setattr__ = __enum_setattr
LubricantDefinition.__delattr__ = __enum_delattr
