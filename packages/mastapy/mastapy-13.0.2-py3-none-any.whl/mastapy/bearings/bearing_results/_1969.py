"""LoadedBallElementPropertyType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LOADED_BALL_ELEMENT_PROPERTY_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBallElementPropertyType"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallElementPropertyType",)


Self = TypeVar("Self", bound="LoadedBallElementPropertyType")


class LoadedBallElementPropertyType(Enum):
    """LoadedBallElementPropertyType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LOADED_BALL_ELEMENT_PROPERTY_TYPE

    ELEMENT_WITH_HIGHEST_SLIDING_SPEED = 0
    ELEMENT_WITH_HIGHEST_PRESSURE_VELOCITY = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LoadedBallElementPropertyType.__setattr__ = __enum_setattr
LoadedBallElementPropertyType.__delattr__ = __enum_delattr
