"""RolledBeforeOrAfterHeatTreatment"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROLLED_BEFORE_OR_AFTER_HEAT_TREATMENT = python_net_import(
    "SMT.MastaAPI.Bolts", "RolledBeforeOrAfterHeatTreatment"
)


__docformat__ = "restructuredtext en"
__all__ = ("RolledBeforeOrAfterHeatTreatment",)


Self = TypeVar("Self", bound="RolledBeforeOrAfterHeatTreatment")


class RolledBeforeOrAfterHeatTreatment(Enum):
    """RolledBeforeOrAfterHeatTreatment

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROLLED_BEFORE_OR_AFTER_HEAT_TREATMENT

    ROLLED_BEFORE_HEAT_TREATMENT = 0
    ROLLED_AFTER_HEAT_TREATMENT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RolledBeforeOrAfterHeatTreatment.__setattr__ = __enum_setattr
RolledBeforeOrAfterHeatTreatment.__delattr__ = __enum_delattr
