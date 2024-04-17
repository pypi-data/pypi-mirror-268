"""ManufacturingTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MANUFACTURING_TYPES = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "ManufacturingTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("ManufacturingTypes",)


Self = TypeVar("Self", bound="ManufacturingTypes")


class ManufacturingTypes(Enum):
    """ManufacturingTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MANUFACTURING_TYPES

    BROACHING = 0
    HOBBING = 1
    GEAR_SHAPING = 2
    COLD_ROLLING = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ManufacturingTypes.__setattr__ = __enum_setattr
ManufacturingTypes.__delattr__ = __enum_delattr
