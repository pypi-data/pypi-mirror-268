"""PIDControlUpdateMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PID_CONTROL_UPDATE_METHOD = python_net_import(
    "SMT.MastaAPI.MathUtility", "PIDControlUpdateMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("PIDControlUpdateMethod",)


Self = TypeVar("Self", bound="PIDControlUpdateMethod")


class PIDControlUpdateMethod(Enum):
    """PIDControlUpdateMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PID_CONTROL_UPDATE_METHOD

    EACH_SOLVER_STEP = 0
    SAMPLE_TIME = 1
    CONTINUOUS = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PIDControlUpdateMethod.__setattr__ = __enum_setattr
PIDControlUpdateMethod.__delattr__ = __enum_delattr
