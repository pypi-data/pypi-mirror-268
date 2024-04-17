"""SMTAxis"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SMT_AXIS = python_net_import("SMT.MastaAPI.UtilityGUI.Charts", "SMTAxis")


__docformat__ = "restructuredtext en"
__all__ = ("SMTAxis",)


Self = TypeVar("Self", bound="SMTAxis")


class SMTAxis(Enum):
    """SMTAxis

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SMT_AXIS

    PRIMARYX = 0
    SECONDARYX = 1
    TERTIARYX = 2
    PRIMARYY = 3
    SECONDARYY = 4
    DEPTH = 5
    POLAR = 6
    POLARANGLE = 7
    I_ = 8
    J = 9
    RESULT = 10


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SMTAxis.__setattr__ = __enum_setattr
SMTAxis.__delattr__ = __enum_delattr
