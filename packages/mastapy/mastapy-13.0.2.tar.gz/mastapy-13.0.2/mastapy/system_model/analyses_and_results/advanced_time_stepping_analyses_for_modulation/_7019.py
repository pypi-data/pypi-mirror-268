"""AtsamExcitationsOrOthers"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ATSAM_EXCITATIONS_OR_OTHERS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AtsamExcitationsOrOthers",
)


__docformat__ = "restructuredtext en"
__all__ = ("AtsamExcitationsOrOthers",)


Self = TypeVar("Self", bound="AtsamExcitationsOrOthers")


class AtsamExcitationsOrOthers(Enum):
    """AtsamExcitationsOrOthers

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ATSAM_EXCITATIONS_OR_OTHERS

    ADVANCED_MODEL = 0
    OTHER_EXCITATIONS = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AtsamExcitationsOrOthers.__setattr__ = __enum_setattr
AtsamExcitationsOrOthers.__delattr__ = __enum_delattr
