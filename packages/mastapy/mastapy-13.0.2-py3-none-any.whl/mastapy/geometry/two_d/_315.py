"""InternalExternalType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_INTERNAL_EXTERNAL_TYPE = python_net_import(
    "SMT.MastaAPI.Geometry.TwoD", "InternalExternalType"
)


__docformat__ = "restructuredtext en"
__all__ = ("InternalExternalType",)


Self = TypeVar("Self", bound="InternalExternalType")


class InternalExternalType(Enum):
    """InternalExternalType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INTERNAL_EXTERNAL_TYPE

    INTERNAL = 0
    EXTERNAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


InternalExternalType.__setattr__ = __enum_setattr
InternalExternalType.__delattr__ = __enum_delattr
