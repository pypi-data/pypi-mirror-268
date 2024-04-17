"""ValueInputOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_VALUE_INPUT_OPTION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "ValueInputOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ValueInputOption",)


Self = TypeVar("Self", bound="ValueInputOption")


class ValueInputOption(Enum):
    """ValueInputOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _VALUE_INPUT_OPTION

    CONSTANT = 0
    VARYING_WITH_TIME = 1
    VARYING_WITH_ANGLE = 2
    VARYING_WITH_POSITION = 3
    VARYING_WITH_ANGLE_AND_SPEED = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ValueInputOption.__setattr__ = __enum_setattr
ValueInputOption.__delattr__ = __enum_delattr
