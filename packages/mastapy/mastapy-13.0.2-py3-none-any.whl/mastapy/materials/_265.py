"""LubricantDelivery"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LUBRICANT_DELIVERY = python_net_import("SMT.MastaAPI.Materials", "LubricantDelivery")


__docformat__ = "restructuredtext en"
__all__ = ("LubricantDelivery",)


Self = TypeVar("Self", bound="LubricantDelivery")


class LubricantDelivery(Enum):
    """LubricantDelivery

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LUBRICANT_DELIVERY

    SEALED = 0
    SPLASH = 1
    FEED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LubricantDelivery.__setattr__ = __enum_setattr
LubricantDelivery.__delattr__ = __enum_delattr
