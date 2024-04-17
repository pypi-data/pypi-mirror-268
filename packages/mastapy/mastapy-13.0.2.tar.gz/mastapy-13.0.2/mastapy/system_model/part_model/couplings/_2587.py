"""ClutchType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CLUTCH_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ClutchType",)


Self = TypeVar("Self", bound="ClutchType")


class ClutchType(Enum):
    """ClutchType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CLUTCH_TYPE

    CONCEPT_CLUTCH = 0
    MULTIPLATE_CLUTCH = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ClutchType.__setattr__ = __enum_setattr
ClutchType.__delattr__ = __enum_delattr
