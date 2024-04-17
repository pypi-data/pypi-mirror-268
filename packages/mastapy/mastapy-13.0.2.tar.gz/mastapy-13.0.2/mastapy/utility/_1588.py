"""ExternalFullFEFileOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_EXTERNAL_FULL_FE_FILE_OPTION = python_net_import(
    "SMT.MastaAPI.Utility", "ExternalFullFEFileOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ExternalFullFEFileOption",)


Self = TypeVar("Self", bound="ExternalFullFEFileOption")


class ExternalFullFEFileOption(Enum):
    """ExternalFullFEFileOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _EXTERNAL_FULL_FE_FILE_OPTION

    NONE = 0
    MESH = 1
    MESH_AND_EXPANSION_VECTORS = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ExternalFullFEFileOption.__setattr__ = __enum_setattr
ExternalFullFEFileOption.__delattr__ = __enum_delattr
