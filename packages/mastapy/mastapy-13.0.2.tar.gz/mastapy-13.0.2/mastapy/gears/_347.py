"""QualityGradeTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_QUALITY_GRADE_TYPES = python_net_import("SMT.MastaAPI.Gears", "QualityGradeTypes")


__docformat__ = "restructuredtext en"
__all__ = ("QualityGradeTypes",)


Self = TypeVar("Self", bound="QualityGradeTypes")


class QualityGradeTypes(Enum):
    """QualityGradeTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _QUALITY_GRADE_TYPES

    AGMA_NEW = 0
    AGMA_OLD = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


QualityGradeTypes.__setattr__ = __enum_setattr
QualityGradeTypes.__delattr__ = __enum_delattr
