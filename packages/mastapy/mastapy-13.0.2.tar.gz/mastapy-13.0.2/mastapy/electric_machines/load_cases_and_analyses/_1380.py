"""SpeedPointsDistribution"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPEED_POINTS_DISTRIBUTION = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SpeedPointsDistribution"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpeedPointsDistribution",)


Self = TypeVar("Self", bound="SpeedPointsDistribution")


class SpeedPointsDistribution(Enum):
    """SpeedPointsDistribution

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPEED_POINTS_DISTRIBUTION

    LINEAR = 0
    USERDEFINED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SpeedPointsDistribution.__setattr__ = __enum_setattr
SpeedPointsDistribution.__delattr__ = __enum_delattr
