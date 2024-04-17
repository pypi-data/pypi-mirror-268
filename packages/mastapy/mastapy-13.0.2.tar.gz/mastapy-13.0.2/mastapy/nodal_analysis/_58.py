"""ElementOrder"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELEMENT_ORDER = python_net_import("SMT.MastaAPI.NodalAnalysis", "ElementOrder")


__docformat__ = "restructuredtext en"
__all__ = ("ElementOrder",)


Self = TypeVar("Self", bound="ElementOrder")


class ElementOrder(Enum):
    """ElementOrder

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELEMENT_ORDER

    LINEAR = 0
    QUADRATIC = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElementOrder.__setattr__ = __enum_setattr
ElementOrder.__delattr__ = __enum_delattr
