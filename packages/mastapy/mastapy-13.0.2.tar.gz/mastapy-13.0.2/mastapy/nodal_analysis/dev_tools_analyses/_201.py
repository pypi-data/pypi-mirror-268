"""MassMatrixType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MASS_MATRIX_TYPE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "MassMatrixType"
)


__docformat__ = "restructuredtext en"
__all__ = ("MassMatrixType",)


Self = TypeVar("Self", bound="MassMatrixType")


class MassMatrixType(Enum):
    """MassMatrixType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MASS_MATRIX_TYPE

    DIAGONAL = 0
    CONSISTENT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MassMatrixType.__setattr__ = __enum_setattr
MassMatrixType.__delattr__ = __enum_delattr
