"""RotationAxis"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROTATION_AXIS = python_net_import("SMT.MastaAPI.MathUtility", "RotationAxis")


__docformat__ = "restructuredtext en"
__all__ = ("RotationAxis",)


Self = TypeVar("Self", bound="RotationAxis")


class RotationAxis(Enum):
    """RotationAxis

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROTATION_AXIS

    X_AXIS = 0
    Y_AXIS = 1
    Z_AXIS = 2
    USERSPECIFIED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RotationAxis.__setattr__ = __enum_setattr
RotationAxis.__delattr__ = __enum_delattr
