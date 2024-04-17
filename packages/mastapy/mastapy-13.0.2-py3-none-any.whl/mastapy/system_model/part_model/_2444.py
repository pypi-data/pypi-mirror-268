"""AGMALoadSharingTableApplicationLevel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_LOAD_SHARING_TABLE_APPLICATION_LEVEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AGMALoadSharingTableApplicationLevel"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMALoadSharingTableApplicationLevel",)


Self = TypeVar("Self", bound="AGMALoadSharingTableApplicationLevel")


class AGMALoadSharingTableApplicationLevel(Enum):
    """AGMALoadSharingTableApplicationLevel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_LOAD_SHARING_TABLE_APPLICATION_LEVEL

    APPLICATION_LEVEL_1 = 0
    APPLICATION_LEVEL_2 = 1
    APPLICATION_LEVEL_3 = 2
    APPLICATION_LEVEL_4 = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMALoadSharingTableApplicationLevel.__setattr__ = __enum_setattr
AGMALoadSharingTableApplicationLevel.__delattr__ = __enum_delattr
