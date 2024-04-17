"""GeometryToExport"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEOMETRY_TO_EXPORT = python_net_import("SMT.MastaAPI.Cycloidal", "GeometryToExport")


__docformat__ = "restructuredtext en"
__all__ = ("GeometryToExport",)


Self = TypeVar("Self", bound="GeometryToExport")


class GeometryToExport(Enum):
    """GeometryToExport

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEOMETRY_TO_EXPORT

    SINGLE_LOBE = 0
    WHOLE_DISC = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GeometryToExport.__setattr__ = __enum_setattr
GeometryToExport.__delattr__ = __enum_delattr
