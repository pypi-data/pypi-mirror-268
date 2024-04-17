"""IndividualContactPosition"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_INDIVIDUAL_CONTACT_POSITION = python_net_import(
    "SMT.MastaAPI.MathUtility.StiffnessCalculators", "IndividualContactPosition"
)


__docformat__ = "restructuredtext en"
__all__ = ("IndividualContactPosition",)


Self = TypeVar("Self", bound="IndividualContactPosition")


class IndividualContactPosition(Enum):
    """IndividualContactPosition

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INDIVIDUAL_CONTACT_POSITION

    LEFT_FLANK = 0
    MAJOR_DIAMETER = 1
    RIGHT_FLANK = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


IndividualContactPosition.__setattr__ = __enum_setattr
IndividualContactPosition.__delattr__ = __enum_delattr
