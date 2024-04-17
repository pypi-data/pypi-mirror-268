"""UseLtcaInAsdOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_USE_LTCA_IN_ASD_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "UseLtcaInAsdOption",
)


__docformat__ = "restructuredtext en"
__all__ = ("UseLtcaInAsdOption",)


Self = TypeVar("Self", bound="UseLtcaInAsdOption")


class UseLtcaInAsdOption(Enum):
    """UseLtcaInAsdOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _USE_LTCA_IN_ASD_OPTION

    NO = 0
    YES = 1
    AUTO = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


UseLtcaInAsdOption.__setattr__ = __enum_setattr
UseLtcaInAsdOption.__delattr__ = __enum_delattr
