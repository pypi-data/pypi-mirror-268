"""AssemblyMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ASSEMBLY_METHODS = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "AssemblyMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyMethods",)


Self = TypeVar("Self", bound="AssemblyMethods")


class AssemblyMethods(Enum):
    """AssemblyMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ASSEMBLY_METHODS

    PRESS_FITTING = 0
    THERMAL_FITTING = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AssemblyMethods.__setattr__ = __enum_setattr
AssemblyMethods.__delattr__ = __enum_delattr
