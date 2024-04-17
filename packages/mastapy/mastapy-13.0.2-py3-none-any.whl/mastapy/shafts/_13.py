"""FkmVersionOfMinersRule"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FKM_VERSION_OF_MINERS_RULE = python_net_import(
    "SMT.MastaAPI.Shafts", "FkmVersionOfMinersRule"
)


__docformat__ = "restructuredtext en"
__all__ = ("FkmVersionOfMinersRule",)


Self = TypeVar("Self", bound="FkmVersionOfMinersRule")


class FkmVersionOfMinersRule(Enum):
    """FkmVersionOfMinersRule

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FKM_VERSION_OF_MINERS_RULE

    CONSISTENT = 0
    ELEMENTARY = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FkmVersionOfMinersRule.__setattr__ = __enum_setattr
FkmVersionOfMinersRule.__delattr__ = __enum_delattr
