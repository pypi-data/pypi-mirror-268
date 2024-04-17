"""AlignmentMethodForRaceBearing"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ALIGNMENT_METHOD_FOR_RACE_BEARING = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "AlignmentMethodForRaceBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("AlignmentMethodForRaceBearing",)


Self = TypeVar("Self", bound="AlignmentMethodForRaceBearing")


class AlignmentMethodForRaceBearing(Enum):
    """AlignmentMethodForRaceBearing

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ALIGNMENT_METHOD_FOR_RACE_BEARING

    MANUAL = 0
    DATUM = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AlignmentMethodForRaceBearing.__setattr__ = __enum_setattr
AlignmentMethodForRaceBearing.__delattr__ = __enum_delattr
