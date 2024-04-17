"""BearingStiffnessModel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_STIFFNESS_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "BearingStiffnessModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingStiffnessModel",)


Self = TypeVar("Self", bound="BearingStiffnessModel")


class BearingStiffnessModel(Enum):
    """BearingStiffnessModel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_STIFFNESS_MODEL

    LINEAR_CONCEPT_BEARINGS = 0
    SYSTEM_DEFLECTION_RESULT = 1
    NONLINEAR_BEARING_MODEL = 2
    LOAD_CASE_SETTING = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingStiffnessModel.__setattr__ = __enum_setattr
BearingStiffnessModel.__delattr__ = __enum_delattr
