"""SystemOptimiserGearSetOptimisation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SYSTEM_OPTIMISER_GEAR_SET_OPTIMISATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "SystemOptimiserGearSetOptimisation",
)


__docformat__ = "restructuredtext en"
__all__ = ("SystemOptimiserGearSetOptimisation",)


Self = TypeVar("Self", bound="SystemOptimiserGearSetOptimisation")


class SystemOptimiserGearSetOptimisation(Enum):
    """SystemOptimiserGearSetOptimisation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SYSTEM_OPTIMISER_GEAR_SET_OPTIMISATION

    NONE = 0
    NORMAL_30_ITERATIONS_OF_MACRO_GEOMETRY_OPTIMISER = 1
    FULL_150_ITERATIONS_OF_MACRO_GEOMETRY_OPTIMISER = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SystemOptimiserGearSetOptimisation.__setattr__ = __enum_setattr
SystemOptimiserGearSetOptimisation.__delattr__ = __enum_delattr
