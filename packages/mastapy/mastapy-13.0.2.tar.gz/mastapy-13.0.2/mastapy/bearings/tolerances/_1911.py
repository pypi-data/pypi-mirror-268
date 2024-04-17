"""BearingToleranceDefinitionOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_TOLERANCE_DEFINITION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "BearingToleranceDefinitionOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingToleranceDefinitionOptions",)


Self = TypeVar("Self", bound="BearingToleranceDefinitionOptions")


class BearingToleranceDefinitionOptions(Enum):
    """BearingToleranceDefinitionOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_TOLERANCE_DEFINITION_OPTIONS

    CLASSES = 0
    VALUES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingToleranceDefinitionOptions.__setattr__ = __enum_setattr
BearingToleranceDefinitionOptions.__delattr__ = __enum_delattr
