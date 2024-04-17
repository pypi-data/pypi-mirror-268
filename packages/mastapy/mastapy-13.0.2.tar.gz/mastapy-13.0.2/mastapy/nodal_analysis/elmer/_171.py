"""ContactType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONTACT_TYPE = python_net_import("SMT.MastaAPI.NodalAnalysis.Elmer", "ContactType")


__docformat__ = "restructuredtext en"
__all__ = ("ContactType",)


Self = TypeVar("Self", bound="ContactType")


class ContactType(Enum):
    """ContactType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_TYPE

    NONE = 0
    TIED = 1
    FRICTION = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ContactType.__setattr__ = __enum_setattr
ContactType.__delattr__ = __enum_delattr
