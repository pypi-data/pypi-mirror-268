"""ContactPairConstrainedSurfaceType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONTACT_PAIR_CONSTRAINED_SURFACE_TYPE = python_net_import(
    "SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums",
    "ContactPairConstrainedSurfaceType",
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactPairConstrainedSurfaceType",)


Self = TypeVar("Self", bound="ContactPairConstrainedSurfaceType")


class ContactPairConstrainedSurfaceType(Enum):
    """ContactPairConstrainedSurfaceType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_PAIR_CONSTRAINED_SURFACE_TYPE

    NONE = 0
    NODE = 1
    ELEMENT_EDGE = 2
    ELEMENT_FACE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ContactPairConstrainedSurfaceType.__setattr__ = __enum_setattr
ContactPairConstrainedSurfaceType.__delattr__ = __enum_delattr
