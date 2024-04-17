"""ComponentOrientationOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COMPONENT_ORIENTATION_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ComponentOrientationOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ComponentOrientationOption",)


Self = TypeVar("Self", bound="ComponentOrientationOption")


class ComponentOrientationOption(Enum):
    """ComponentOrientationOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COMPONENT_ORIENTATION_OPTION

    DO_NOT_CHANGE = 0
    ALIGN_WITH_FE_AXES = 1
    ALIGN_NORMAL_TO_FE_SURFACE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ComponentOrientationOption.__setattr__ = __enum_setattr
ComponentOrientationOption.__delattr__ = __enum_delattr
