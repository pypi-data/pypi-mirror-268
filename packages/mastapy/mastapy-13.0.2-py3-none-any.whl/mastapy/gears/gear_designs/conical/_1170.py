"""FrontEndTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FRONT_END_TYPES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "FrontEndTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("FrontEndTypes",)


Self = TypeVar("Self", bound="FrontEndTypes")


class FrontEndTypes(Enum):
    """FrontEndTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FRONT_END_TYPES

    FLAT = 0
    CONICAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FrontEndTypes.__setattr__ = __enum_setattr
FrontEndTypes.__delattr__ = __enum_delattr
