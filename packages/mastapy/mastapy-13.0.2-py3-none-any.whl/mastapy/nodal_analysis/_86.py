"""ResultLoggingFrequency"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RESULT_LOGGING_FREQUENCY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "ResultLoggingFrequency"
)


__docformat__ = "restructuredtext en"
__all__ = ("ResultLoggingFrequency",)


Self = TypeVar("Self", bound="ResultLoggingFrequency")


class ResultLoggingFrequency(Enum):
    """ResultLoggingFrequency

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RESULT_LOGGING_FREQUENCY

    ALL = 0
    IGNORE_SMALL_STEPS = 1
    NONE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ResultLoggingFrequency.__setattr__ = __enum_setattr
ResultLoggingFrequency.__delattr__ = __enum_delattr
