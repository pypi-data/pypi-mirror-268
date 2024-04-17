"""ToothTaperSpecification"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TOOTH_TAPER_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ToothTaperSpecification"
)


__docformat__ = "restructuredtext en"
__all__ = ("ToothTaperSpecification",)


Self = TypeVar("Self", bound="ToothTaperSpecification")


class ToothTaperSpecification(Enum):
    """ToothTaperSpecification

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TOOTH_TAPER_SPECIFICATION

    DEPTH = 0
    ANGLE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ToothTaperSpecification.__setattr__ = __enum_setattr
ToothTaperSpecification.__delattr__ = __enum_delattr
