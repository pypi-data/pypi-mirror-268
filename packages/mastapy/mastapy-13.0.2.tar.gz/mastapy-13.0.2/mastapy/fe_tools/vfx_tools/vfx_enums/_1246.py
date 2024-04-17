"""ProSolveSolverType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PRO_SOLVE_SOLVER_TYPE = python_net_import(
    "SMT.MastaAPI.FETools.VfxTools.VfxEnums", "ProSolveSolverType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ProSolveSolverType",)


Self = TypeVar("Self", bound="ProSolveSolverType")


class ProSolveSolverType(Enum):
    """ProSolveSolverType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PRO_SOLVE_SOLVER_TYPE

    LEFTLOOKING = 4
    SERIAL_MULTIFRONTAL = 5
    PARALLEL_MULTIFRONTAL = 6


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ProSolveSolverType.__setattr__ = __enum_setattr
ProSolveSolverType.__delattr__ = __enum_delattr
