"""FESurfaceDrawingOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_SURFACE_DRAWING_OPTION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FESurfaceDrawingOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("FESurfaceDrawingOption",)


Self = TypeVar("Self", bound="FESurfaceDrawingOption")


class FESurfaceDrawingOption(Enum):
    """FESurfaceDrawingOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_SURFACE_DRAWING_OPTION

    NONE = 0
    TRANSPARENT = 1
    SOLID = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FESurfaceDrawingOption.__setattr__ = __enum_setattr
FESurfaceDrawingOption.__delattr__ = __enum_delattr
