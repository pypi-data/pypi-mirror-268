"""SoundPressureEnclosureType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SOUND_PRESSURE_ENCLOSURE_TYPE = python_net_import(
    "SMT.MastaAPI.Materials", "SoundPressureEnclosureType"
)


__docformat__ = "restructuredtext en"
__all__ = ("SoundPressureEnclosureType",)


Self = TypeVar("Self", bound="SoundPressureEnclosureType")


class SoundPressureEnclosureType(Enum):
    """SoundPressureEnclosureType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SOUND_PRESSURE_ENCLOSURE_TYPE

    FREE_FIELD = 0
    FREE_FIELD_OVER_REFLECTING_PLANE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SoundPressureEnclosureType.__setattr__ = __enum_setattr
SoundPressureEnclosureType.__delattr__ = __enum_delattr
