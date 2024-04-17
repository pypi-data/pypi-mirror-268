"""JointTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_JOINT_TYPES = python_net_import("SMT.MastaAPI.Bolts", "JointTypes")


__docformat__ = "restructuredtext en"
__all__ = ("JointTypes",)


Self = TypeVar("Self", bound="JointTypes")


class JointTypes(Enum):
    """JointTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _JOINT_TYPES

    SV1 = 0
    SV2 = 1
    SV3 = 2
    SV4 = 3
    SV5 = 4
    SV6 = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


JointTypes.__setattr__ = __enum_setattr
JointTypes.__delattr__ = __enum_delattr
