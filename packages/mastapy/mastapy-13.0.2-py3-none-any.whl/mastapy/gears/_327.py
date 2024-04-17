"""CylindricalMisalignmentDataSource"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MISALIGNMENT_DATA_SOURCE = python_net_import(
    "SMT.MastaAPI.Gears", "CylindricalMisalignmentDataSource"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMisalignmentDataSource",)


Self = TypeVar("Self", bound="CylindricalMisalignmentDataSource")


class CylindricalMisalignmentDataSource(Enum):
    """CylindricalMisalignmentDataSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_MISALIGNMENT_DATA_SOURCE

    STANDARD = 0
    USERSPECIFIED = 1
    SYSTEM_DEFLECTION = 2
    ADVANCED_SYSTEM_DEFLECTION = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalMisalignmentDataSource.__setattr__ = __enum_setattr
CylindricalMisalignmentDataSource.__delattr__ = __enum_delattr
