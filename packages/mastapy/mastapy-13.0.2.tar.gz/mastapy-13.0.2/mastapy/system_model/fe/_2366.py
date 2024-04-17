"""AngleSource"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ANGLE_SOURCE = python_net_import("SMT.MastaAPI.SystemModel.FE", "AngleSource")


__docformat__ = "restructuredtext en"
__all__ = ("AngleSource",)


Self = TypeVar("Self", bound="AngleSource")


class AngleSource(Enum):
    """AngleSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ANGLE_SOURCE

    SPECIFIED_VALUE = 0
    DERIVED = 1
    INDEX = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AngleSource.__setattr__ = __enum_setattr
AngleSource.__delattr__ = __enum_delattr
