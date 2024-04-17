"""MotoringOrGenerating"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MOTORING_OR_GENERATING = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "MotoringOrGenerating"
)


__docformat__ = "restructuredtext en"
__all__ = ("MotoringOrGenerating",)


Self = TypeVar("Self", bound="MotoringOrGenerating")


class MotoringOrGenerating(Enum):
    """MotoringOrGenerating

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MOTORING_OR_GENERATING

    MOTORING = 0
    GENERATING = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MotoringOrGenerating.__setattr__ = __enum_setattr
MotoringOrGenerating.__delattr__ = __enum_delattr
