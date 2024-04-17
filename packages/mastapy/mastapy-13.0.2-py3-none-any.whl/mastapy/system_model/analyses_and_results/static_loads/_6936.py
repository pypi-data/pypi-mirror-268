"""ParametricStudyType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ParametricStudyType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyType",)


Self = TypeVar("Self", bound="ParametricStudyType")


class ParametricStudyType(Enum):
    """ParametricStudyType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PARAMETRIC_STUDY_TYPE

    LINEAR_SWEEP = 0
    MONTE_CARLO = 1
    DESIGN_OF_EXPERIMENTS = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ParametricStudyType.__setattr__ = __enum_setattr
ParametricStudyType.__delattr__ = __enum_delattr
