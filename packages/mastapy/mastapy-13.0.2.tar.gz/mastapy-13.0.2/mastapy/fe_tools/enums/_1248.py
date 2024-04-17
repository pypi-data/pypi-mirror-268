"""MaterialPropertyClass"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MATERIAL_PROPERTY_CLASS = python_net_import(
    "SMT.MastaAPI.FETools.Enums", "MaterialPropertyClass"
)


__docformat__ = "restructuredtext en"
__all__ = ("MaterialPropertyClass",)


Self = TypeVar("Self", bound="MaterialPropertyClass")


class MaterialPropertyClass(Enum):
    """MaterialPropertyClass

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MATERIAL_PROPERTY_CLASS

    ISOTROPIC = 0
    ORTHOTROPIC = 2
    ANISOTROPIC = 3
    HYPERELASTIC = 4
    UNKNOWN_CLASS = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MaterialPropertyClass.__setattr__ = __enum_setattr
MaterialPropertyClass.__delattr__ = __enum_delattr
