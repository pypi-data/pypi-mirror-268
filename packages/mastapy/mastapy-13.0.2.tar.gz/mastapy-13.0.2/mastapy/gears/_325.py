"""ContactRatioRequirements"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONTACT_RATIO_REQUIREMENTS = python_net_import(
    "SMT.MastaAPI.Gears", "ContactRatioRequirements"
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactRatioRequirements",)


Self = TypeVar("Self", bound="ContactRatioRequirements")


class ContactRatioRequirements(Enum):
    """ContactRatioRequirements

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_RATIO_REQUIREMENTS

    MAXIMISE = 0
    IGNORE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ContactRatioRequirements.__setattr__ = __enum_setattr
ContactRatioRequirements.__delattr__ = __enum_delattr
