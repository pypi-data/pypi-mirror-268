"""ConsequenceOfFailure"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONSEQUENCE_OF_FAILURE = python_net_import(
    "SMT.MastaAPI.Shafts", "ConsequenceOfFailure"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConsequenceOfFailure",)


Self = TypeVar("Self", bound="ConsequenceOfFailure")


class ConsequenceOfFailure(Enum):
    """ConsequenceOfFailure

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONSEQUENCE_OF_FAILURE

    SEVERE = 0
    MEAN = 1
    MODERATE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ConsequenceOfFailure.__setattr__ = __enum_setattr
ConsequenceOfFailure.__delattr__ = __enum_delattr
