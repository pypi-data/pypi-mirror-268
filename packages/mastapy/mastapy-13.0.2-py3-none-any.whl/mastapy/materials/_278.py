"""MetalPlasticType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_METAL_PLASTIC_TYPE = python_net_import("SMT.MastaAPI.Materials", "MetalPlasticType")


__docformat__ = "restructuredtext en"
__all__ = ("MetalPlasticType",)


Self = TypeVar("Self", bound="MetalPlasticType")


class MetalPlasticType(Enum):
    """MetalPlasticType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _METAL_PLASTIC_TYPE

    PLASTIC = 0
    METAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MetalPlasticType.__setattr__ = __enum_setattr
MetalPlasticType.__delattr__ = __enum_delattr
