"""InputSignalFilterLevel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_INPUT_SIGNAL_FILTER_LEVEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "InputSignalFilterLevel"
)


__docformat__ = "restructuredtext en"
__all__ = ("InputSignalFilterLevel",)


Self = TypeVar("Self", bound="InputSignalFilterLevel")


class InputSignalFilterLevel(Enum):
    """InputSignalFilterLevel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INPUT_SIGNAL_FILTER_LEVEL

    NONE = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


InputSignalFilterLevel.__setattr__ = __enum_setattr
InputSignalFilterLevel.__delattr__ = __enum_delattr
