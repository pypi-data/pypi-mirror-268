"""CutterMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CUTTER_METHOD = python_net_import("SMT.MastaAPI.GleasonSMTLink", "CutterMethod")


__docformat__ = "restructuredtext en"
__all__ = ("CutterMethod",)


Self = TypeVar("Self", bound="CutterMethod")


class CutterMethod(Enum):
    """CutterMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CUTTER_METHOD

    FACE_MILLING = 1
    FACE_HOBBING = 9


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CutterMethod.__setattr__ = __enum_setattr
CutterMethod.__delattr__ = __enum_delattr
