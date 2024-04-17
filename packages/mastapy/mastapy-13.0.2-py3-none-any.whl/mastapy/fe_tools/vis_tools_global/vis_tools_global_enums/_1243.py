"""ElementPropertiesShellWallType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SHELL_WALL_TYPE = python_net_import(
    "SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums",
    "ElementPropertiesShellWallType",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesShellWallType",)


Self = TypeVar("Self", bound="ElementPropertiesShellWallType")


class ElementPropertiesShellWallType(Enum):
    """ElementPropertiesShellWallType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELEMENT_PROPERTIES_SHELL_WALL_TYPE

    MONOCOQUE = 0
    LAMINATED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElementPropertiesShellWallType.__setattr__ = __enum_setattr
ElementPropertiesShellWallType.__delattr__ = __enum_delattr
