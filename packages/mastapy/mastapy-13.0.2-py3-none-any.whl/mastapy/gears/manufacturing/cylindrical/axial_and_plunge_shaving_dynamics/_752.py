"""ActiveProfileRangeCalculationSource"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ACTIVE_PROFILE_RANGE_CALCULATION_SOURCE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ActiveProfileRangeCalculationSource",
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveProfileRangeCalculationSource",)


Self = TypeVar("Self", bound="ActiveProfileRangeCalculationSource")


class ActiveProfileRangeCalculationSource(Enum):
    """ActiveProfileRangeCalculationSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ACTIVE_PROFILE_RANGE_CALCULATION_SOURCE

    DESIGNED_GEAR_WITHOUT_TOLERANCES = 0
    MANUFACTURED_GEAR_WITH_TOLERANCES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ActiveProfileRangeCalculationSource.__setattr__ = __enum_setattr
ActiveProfileRangeCalculationSource.__delattr__ = __enum_delattr
