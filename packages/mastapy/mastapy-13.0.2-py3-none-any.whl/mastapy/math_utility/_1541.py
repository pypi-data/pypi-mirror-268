"""TranslationRotation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TRANSLATION_ROTATION = python_net_import(
    "SMT.MastaAPI.MathUtility", "TranslationRotation"
)


__docformat__ = "restructuredtext en"
__all__ = ("TranslationRotation",)


Self = TypeVar("Self", bound="TranslationRotation")


class TranslationRotation(Enum):
    """TranslationRotation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TRANSLATION_ROTATION

    TRANSLATION = 0
    ROTATION = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TranslationRotation.__setattr__ = __enum_setattr
TranslationRotation.__delattr__ = __enum_delattr
