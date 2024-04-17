"""ContactPairReferenceSurfaceType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONTACT_PAIR_REFERENCE_SURFACE_TYPE = python_net_import(
    "SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums",
    "ContactPairReferenceSurfaceType",
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactPairReferenceSurfaceType",)


Self = TypeVar("Self", bound="ContactPairReferenceSurfaceType")


class ContactPairReferenceSurfaceType(Enum):
    """ContactPairReferenceSurfaceType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_PAIR_REFERENCE_SURFACE_TYPE

    ELEMENT_EDGE = 2
    ELEMENT_FACE = 3
    ANALYTIC_SURFACE = 2660


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ContactPairReferenceSurfaceType.__setattr__ = __enum_setattr
ContactPairReferenceSurfaceType.__delattr__ = __enum_delattr
