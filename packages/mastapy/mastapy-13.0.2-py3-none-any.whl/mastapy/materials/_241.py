"""AcousticRadiationEfficiencyInputType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ACOUSTIC_RADIATION_EFFICIENCY_INPUT_TYPE = python_net_import(
    "SMT.MastaAPI.Materials", "AcousticRadiationEfficiencyInputType"
)


__docformat__ = "restructuredtext en"
__all__ = ("AcousticRadiationEfficiencyInputType",)


Self = TypeVar("Self", bound="AcousticRadiationEfficiencyInputType")


class AcousticRadiationEfficiencyInputType(Enum):
    """AcousticRadiationEfficiencyInputType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ACOUSTIC_RADIATION_EFFICIENCY_INPUT_TYPE

    SPECIFY_VALUES = 0
    SIMPLE_PARAMETRISED = 1
    UNITY = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AcousticRadiationEfficiencyInputType.__setattr__ = __enum_setattr
AcousticRadiationEfficiencyInputType.__delattr__ = __enum_delattr
