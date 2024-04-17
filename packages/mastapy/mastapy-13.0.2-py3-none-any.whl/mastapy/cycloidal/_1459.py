"""CrowningSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CROWNING_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CrowningSpecificationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("CrowningSpecificationMethod",)


Self = TypeVar("Self", bound="CrowningSpecificationMethod")


class CrowningSpecificationMethod(Enum):
    """CrowningSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CROWNING_SPECIFICATION_METHOD

    CIRCULAR = 0
    LOGARITHMIC = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CrowningSpecificationMethod.__setattr__ = __enum_setattr
CrowningSpecificationMethod.__delattr__ = __enum_delattr
