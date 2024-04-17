"""ParabolicTipReliefStartsTangentToMainProfileRelief"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PARABOLIC_TIP_RELIEF_STARTS_TANGENT_TO_MAIN_PROFILE_RELIEF = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParabolicTipReliefStartsTangentToMainProfileRelief",)


Self = TypeVar("Self", bound="ParabolicTipReliefStartsTangentToMainProfileRelief")


class ParabolicTipReliefStartsTangentToMainProfileRelief(Enum):
    """ParabolicTipReliefStartsTangentToMainProfileRelief

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PARABOLIC_TIP_RELIEF_STARTS_TANGENT_TO_MAIN_PROFILE_RELIEF

    NO = 0
    YES = 1
    ONLY_WHEN_NONZERO_PARABOLIC_TIP_RELIEF = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ParabolicTipReliefStartsTangentToMainProfileRelief.__setattr__ = __enum_setattr
ParabolicTipReliefStartsTangentToMainProfileRelief.__delattr__ = __enum_delattr
