"""VolumeElementShape"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_VOLUME_ELEMENT_SHAPE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "VolumeElementShape"
)


__docformat__ = "restructuredtext en"
__all__ = ("VolumeElementShape",)


Self = TypeVar("Self", bound="VolumeElementShape")


class VolumeElementShape(Enum):
    """VolumeElementShape

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _VOLUME_ELEMENT_SHAPE

    TETRAHEDRAL = 0
    HEXAHEDRAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


VolumeElementShape.__setattr__ = __enum_setattr
VolumeElementShape.__delattr__ = __enum_delattr
