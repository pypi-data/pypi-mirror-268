"""VDI2736LubricantType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_VDI2736_LUBRICANT_TYPE = python_net_import(
    "SMT.MastaAPI.Materials", "VDI2736LubricantType"
)


__docformat__ = "restructuredtext en"
__all__ = ("VDI2736LubricantType",)


Self = TypeVar("Self", bound="VDI2736LubricantType")


class VDI2736LubricantType(Enum):
    """VDI2736LubricantType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _VDI2736_LUBRICANT_TYPE

    OIL = 0
    GREASE = 1
    WATEROIL_EMULSION = 2
    OIL_MIST = 3
    NONE_DRY_RUNNING = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


VDI2736LubricantType.__setattr__ = __enum_setattr
VDI2736LubricantType.__delattr__ = __enum_delattr
