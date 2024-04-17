"""ProSolveMpcType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PRO_SOLVE_MPC_TYPE = python_net_import(
    "SMT.MastaAPI.FETools.VfxTools.VfxEnums", "ProSolveMpcType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ProSolveMpcType",)


Self = TypeVar("Self", bound="ProSolveMpcType")


class ProSolveMpcType(Enum):
    """ProSolveMpcType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PRO_SOLVE_MPC_TYPE

    PENALTY_FUNCTION_METHOD = 1
    LAGRANGE_MULTIPLIER_METHOD = 2
    AUGMENTED_LAGRANGE_MULTIPLIER_METHOD = 3
    MATRIX_TRANSFORMATION_METHOD = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ProSolveMpcType.__setattr__ = __enum_setattr
ProSolveMpcType.__delattr__ = __enum_delattr
