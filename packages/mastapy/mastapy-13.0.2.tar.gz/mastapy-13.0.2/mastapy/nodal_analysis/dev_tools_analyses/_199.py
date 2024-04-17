"""FESurfaceAndNonDeformedDrawingOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_SURFACE_AND_NON_DEFORMED_DRAWING_OPTION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses",
    "FESurfaceAndNonDeformedDrawingOption",
)


__docformat__ = "restructuredtext en"
__all__ = ("FESurfaceAndNonDeformedDrawingOption",)


Self = TypeVar("Self", bound="FESurfaceAndNonDeformedDrawingOption")


class FESurfaceAndNonDeformedDrawingOption(Enum):
    """FESurfaceAndNonDeformedDrawingOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_SURFACE_AND_NON_DEFORMED_DRAWING_OPTION

    NONE = 0
    TRANSPARENT_DEFORMED = 1
    SOLID_DEFORMED = 2
    TRANSPARENT_DEFORMEDTRANSPARENT_NONDEFORMED = 3
    SOLID_DEFORMEDTRANSPARENT_NONDEFORMED = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FESurfaceAndNonDeformedDrawingOption.__setattr__ = __enum_setattr
FESurfaceAndNonDeformedDrawingOption.__delattr__ = __enum_delattr
