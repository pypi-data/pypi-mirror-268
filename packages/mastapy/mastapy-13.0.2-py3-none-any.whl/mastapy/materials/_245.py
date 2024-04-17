"""AGMAMaterialGrade"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_MATERIAL_GRADE = python_net_import("SMT.MastaAPI.Materials", "AGMAMaterialGrade")


__docformat__ = "restructuredtext en"
__all__ = ("AGMAMaterialGrade",)


Self = TypeVar("Self", bound="AGMAMaterialGrade")


class AGMAMaterialGrade(Enum):
    """AGMAMaterialGrade

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_MATERIAL_GRADE

    GRADE_1 = 0
    GRADE_2 = 1
    GRADE_3 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMAMaterialGrade.__setattr__ = __enum_setattr
AGMAMaterialGrade.__delattr__ = __enum_delattr
