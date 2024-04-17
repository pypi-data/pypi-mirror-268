"""OperatingPointsSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_OPERATING_POINTS_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "OperatingPointsSpecificationMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("OperatingPointsSpecificationMethod",)


Self = TypeVar("Self", bound="OperatingPointsSpecificationMethod")


class OperatingPointsSpecificationMethod(Enum):
    """OperatingPointsSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OPERATING_POINTS_SPECIFICATION_METHOD

    USERDEFINED = 0
    ALONG_MAXIMUM_SPEED_TORQUE_CURVE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


OperatingPointsSpecificationMethod.__setattr__ = __enum_setattr
OperatingPointsSpecificationMethod.__delattr__ = __enum_delattr
