"""ClutchSpringType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CLUTCH_SPRING_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "ClutchSpringType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ClutchSpringType",)


Self = TypeVar("Self", bound="ClutchSpringType")


class ClutchSpringType(Enum):
    """ClutchSpringType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CLUTCH_SPRING_TYPE

    NONE = 0
    SPRUNG_APART = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ClutchSpringType.__setattr__ = __enum_setattr
ClutchSpringType.__delattr__ = __enum_delattr
