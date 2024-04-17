"""HobEdgeTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HOB_EDGE_TYPES = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "HobEdgeTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("HobEdgeTypes",)


Self = TypeVar("Self", bound="HobEdgeTypes")


class HobEdgeTypes(Enum):
    """HobEdgeTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HOB_EDGE_TYPES

    ARC = 0
    CATMULLROM_SPLINE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HobEdgeTypes.__setattr__ = __enum_setattr
HobEdgeTypes.__delattr__ = __enum_delattr
