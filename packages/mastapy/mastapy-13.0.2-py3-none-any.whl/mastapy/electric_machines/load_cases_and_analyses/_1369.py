"""EndWindingInductanceMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_END_WINDING_INDUCTANCE_METHOD = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "EndWindingInductanceMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("EndWindingInductanceMethod",)


Self = TypeVar("Self", bound="EndWindingInductanceMethod")


class EndWindingInductanceMethod(Enum):
    """EndWindingInductanceMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _END_WINDING_INDUCTANCE_METHOD

    NONE = 0
    ROSA_AND_GROVER = 1
    USERSPECIFIED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


EndWindingInductanceMethod.__setattr__ = __enum_setattr
EndWindingInductanceMethod.__delattr__ = __enum_delattr
