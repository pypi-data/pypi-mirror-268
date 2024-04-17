"""LoadingStatus"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LOADING_STATUS = python_net_import("SMT.MastaAPI.NodalAnalysis", "LoadingStatus")


__docformat__ = "restructuredtext en"
__all__ = ("LoadingStatus",)


Self = TypeVar("Self", bound="LoadingStatus")


class LoadingStatus(Enum):
    """LoadingStatus

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LOADING_STATUS

    UNLOADED = 0
    LOADED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LoadingStatus.__setattr__ = __enum_setattr
LoadingStatus.__delattr__ = __enum_delattr
