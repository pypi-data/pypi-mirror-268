"""BoundaryConditionType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BOUNDARY_CONDITION_TYPE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.FeExportUtility", "BoundaryConditionType"
)


__docformat__ = "restructuredtext en"
__all__ = ("BoundaryConditionType",)


Self = TypeVar("Self", bound="BoundaryConditionType")


class BoundaryConditionType(Enum):
    """BoundaryConditionType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BOUNDARY_CONDITION_TYPE

    FORCE = 0
    DISPLACEMENT = 1
    NONE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BoundaryConditionType.__setattr__ = __enum_setattr
BoundaryConditionType.__delattr__ = __enum_delattr
