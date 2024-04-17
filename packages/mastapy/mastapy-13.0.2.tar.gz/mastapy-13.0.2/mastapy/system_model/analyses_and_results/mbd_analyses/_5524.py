"""WheelSlipType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_WHEEL_SLIP_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "WheelSlipType"
)


__docformat__ = "restructuredtext en"
__all__ = ("WheelSlipType",)


Self = TypeVar("Self", bound="WheelSlipType")


class WheelSlipType(Enum):
    """WheelSlipType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WHEEL_SLIP_TYPE

    NO_SLIP = 0
    BASIC_SLIP = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


WheelSlipType.__setattr__ = __enum_setattr
WheelSlipType.__delattr__ = __enum_delattr
