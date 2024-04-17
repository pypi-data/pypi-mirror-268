"""ConicalManufactureMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURE_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalManufactureMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalManufactureMethods",)


Self = TypeVar("Self", bound="ConicalManufactureMethods")


class ConicalManufactureMethods(Enum):
    """ConicalManufactureMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONICAL_MANUFACTURE_METHODS

    FORMATE_TILT = 0
    FORMATE_MODIFIED_ROLL = 1
    GENERATING_TILT = 2
    GENERATING_TILT_WITH_OFFSET = 3
    GENERATING_MODIFIED_ROLL = 4
    HELIXFORM = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ConicalManufactureMethods.__setattr__ = __enum_setattr
ConicalManufactureMethods.__delattr__ = __enum_delattr
