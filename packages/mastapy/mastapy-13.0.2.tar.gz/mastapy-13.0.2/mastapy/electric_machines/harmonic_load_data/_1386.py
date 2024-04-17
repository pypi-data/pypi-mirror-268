"""ForceDisplayOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FORCE_DISPLAY_OPTION = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "ForceDisplayOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceDisplayOption",)


Self = TypeVar("Self", bound="ForceDisplayOption")


class ForceDisplayOption(Enum):
    """ForceDisplayOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FORCE_DISPLAY_OPTION

    INDIVIDUAL = 0
    ALL = 1
    SUM = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ForceDisplayOption.__setattr__ = __enum_setattr
ForceDisplayOption.__delattr__ = __enum_delattr
