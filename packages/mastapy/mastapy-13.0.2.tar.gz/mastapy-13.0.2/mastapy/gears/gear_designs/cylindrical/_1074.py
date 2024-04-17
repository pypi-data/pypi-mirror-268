"""ResidualStressCalculationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RESIDUAL_STRESS_CALCULATION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ResidualStressCalculationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("ResidualStressCalculationMethod",)


Self = TypeVar("Self", bound="ResidualStressCalculationMethod")


class ResidualStressCalculationMethod(Enum):
    """ResidualStressCalculationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RESIDUAL_STRESS_CALCULATION_METHOD

    MACKALDENER = 0
    LANG = 1
    MULLER_ET_AL = 2
    USERSPECIFIED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ResidualStressCalculationMethod.__setattr__ = __enum_setattr
ResidualStressCalculationMethod.__delattr__ = __enum_delattr
