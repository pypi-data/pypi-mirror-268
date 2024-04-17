"""NoneSelectedAllOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_NONE_SELECTED_ALL_OPTION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "NoneSelectedAllOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("NoneSelectedAllOption",)


Self = TypeVar("Self", bound="NoneSelectedAllOption")


class NoneSelectedAllOption(Enum):
    """NoneSelectedAllOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _NONE_SELECTED_ALL_OPTION

    NONE = 0
    SELECTED = 1
    ALL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


NoneSelectedAllOption.__setattr__ = __enum_setattr
NoneSelectedAllOption.__delattr__ = __enum_delattr
