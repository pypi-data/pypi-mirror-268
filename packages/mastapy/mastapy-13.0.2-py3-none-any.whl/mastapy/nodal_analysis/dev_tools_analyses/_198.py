"""FESelectionMode"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_SELECTION_MODE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FESelectionMode"
)


__docformat__ = "restructuredtext en"
__all__ = ("FESelectionMode",)


Self = TypeVar("Self", bound="FESelectionMode")


class FESelectionMode(Enum):
    """FESelectionMode

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_SELECTION_MODE

    COMPONENT = 0
    NODE_INDIVIDUAL = 1
    NODE_REGION = 2
    SURFACE = 3
    FACE = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FESelectionMode.__setattr__ = __enum_setattr
FESelectionMode.__delattr__ = __enum_delattr
