"""DefaultOrUserInput"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DEFAULT_OR_USER_INPUT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "DefaultOrUserInput"
)


__docformat__ = "restructuredtext en"
__all__ = ("DefaultOrUserInput",)


Self = TypeVar("Self", bound="DefaultOrUserInput")


class DefaultOrUserInput(Enum):
    """DefaultOrUserInput

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DEFAULT_OR_USER_INPUT

    DIN_STANDARD_DEFAULT = 0
    USERSPECIFIED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DefaultOrUserInput.__setattr__ = __enum_setattr
DefaultOrUserInput.__delattr__ = __enum_delattr
