"""TighteningTechniques"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TIGHTENING_TECHNIQUES = python_net_import("SMT.MastaAPI.Bolts", "TighteningTechniques")


__docformat__ = "restructuredtext en"
__all__ = ("TighteningTechniques",)


Self = TypeVar("Self", bound="TighteningTechniques")


class TighteningTechniques(Enum):
    """TighteningTechniques

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TIGHTENING_TECHNIQUES

    ULTRASOUND_ELONGATION_CONTROLLED_TIGHTENING = 0
    MECHANICAL_ELONGATION_CONTROLLED_TIGHTENING = 1
    YIELD_CONTROLLED_TIGHTENING = 2
    ANGLE_CONTROLLED_TIGHTENING = 3
    HYDRAULIC_TIGHTENING = 4
    TORQUE_WRENCH_WITH_TIGHTENING_TORQUE_EXPERIMENTALLY_DETERMINED = 5
    TORQUE_WRENCH_WITH_ESTIMATED_FRICTION_COEFFICIENT_OF_CLASS_B = 6
    TORQUE_WRENCH_WITH_ESTIMATED_FRICTION_COEFFICIENT_OF_CLASS_A = 7
    IMPACT_WRENCH_TIGHTENING = 8


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TighteningTechniques.__setattr__ = __enum_setattr
TighteningTechniques.__delattr__ = __enum_delattr
