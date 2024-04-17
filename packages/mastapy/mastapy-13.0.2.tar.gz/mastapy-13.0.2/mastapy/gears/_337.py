"""ISOToleranceStandard"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ISO_TOLERANCE_STANDARD = python_net_import(
    "SMT.MastaAPI.Gears", "ISOToleranceStandard"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISOToleranceStandard",)


Self = TypeVar("Self", bound="ISOToleranceStandard")


class ISOToleranceStandard(Enum):
    """ISOToleranceStandard

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ISO_TOLERANCE_STANDARD

    ISO_132811995EISO_132821997E = 0
    ISO_132812013EISO_132821997E = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ISOToleranceStandard.__setattr__ = __enum_setattr
ISOToleranceStandard.__delattr__ = __enum_delattr
