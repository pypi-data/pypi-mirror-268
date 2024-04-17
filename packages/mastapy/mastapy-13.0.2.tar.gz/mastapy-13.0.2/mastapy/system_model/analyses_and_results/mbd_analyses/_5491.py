"""RunUpDrivingMode"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RUN_UP_DRIVING_MODE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "RunUpDrivingMode"
)


__docformat__ = "restructuredtext en"
__all__ = ("RunUpDrivingMode",)


Self = TypeVar("Self", bound="RunUpDrivingMode")


class RunUpDrivingMode(Enum):
    """RunUpDrivingMode

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RUN_UP_DRIVING_MODE

    TORQUE = 0
    SPEED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RunUpDrivingMode.__setattr__ = __enum_setattr
RunUpDrivingMode.__delattr__ = __enum_delattr
