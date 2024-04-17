"""AcousticWeighting"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ACOUSTIC_WEIGHTING = python_net_import("SMT.MastaAPI.MathUtility", "AcousticWeighting")


__docformat__ = "restructuredtext en"
__all__ = ("AcousticWeighting",)


Self = TypeVar("Self", bound="AcousticWeighting")


class AcousticWeighting(Enum):
    """AcousticWeighting

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ACOUSTIC_WEIGHTING

    NONE = 0
    AWEIGHTING = 1
    BWEIGHTING = 2
    CWEIGHTING = 3
    DWEIGHTING = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AcousticWeighting.__setattr__ = __enum_setattr
AcousticWeighting.__delattr__ = __enum_delattr
