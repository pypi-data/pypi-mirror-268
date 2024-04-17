"""Severity"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SEVERITY = python_net_import("SMT.MastaAPI.Utility.ModelValidation", "Severity")


__docformat__ = "restructuredtext en"
__all__ = ("Severity",)


Self = TypeVar("Self", bound="Severity")


class Severity(Enum):
    """Severity

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SEVERITY

    INFORMATION = 1
    WARNING = 2
    ERROR = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


Severity.__setattr__ = __enum_setattr
Severity.__delattr__ = __enum_delattr
