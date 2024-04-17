"""TransientSolverToleranceInputMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TRANSIENT_SOLVER_TOLERANCE_INPUT_METHOD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "TransientSolverToleranceInputMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("TransientSolverToleranceInputMethod",)


Self = TypeVar("Self", bound="TransientSolverToleranceInputMethod")


class TransientSolverToleranceInputMethod(Enum):
    """TransientSolverToleranceInputMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TRANSIENT_SOLVER_TOLERANCE_INPUT_METHOD

    SIMPLE = 0
    ADVANCED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TransientSolverToleranceInputMethod.__setattr__ = __enum_setattr
TransientSolverToleranceInputMethod.__delattr__ = __enum_delattr
