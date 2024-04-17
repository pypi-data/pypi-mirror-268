"""AGMAToleranceStandard"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_TOLERANCE_STANDARD = python_net_import(
    "SMT.MastaAPI.Gears", "AGMAToleranceStandard"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAToleranceStandard",)


Self = TypeVar("Self", bound="AGMAToleranceStandard")


class AGMAToleranceStandard(Enum):
    """AGMAToleranceStandard

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_TOLERANCE_STANDARD

    AGMA_20151A01 = 0
    AGMA_2000A88 = 1
    ANSIAGMA_ISO_13281B14 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMAToleranceStandard.__setattr__ = __enum_setattr
AGMAToleranceStandard.__delattr__ = __enum_delattr
