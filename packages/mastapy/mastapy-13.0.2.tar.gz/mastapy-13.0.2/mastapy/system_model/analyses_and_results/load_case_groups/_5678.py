"""SystemOptimiserTargets"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SYSTEM_OPTIMISER_TARGETS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "SystemOptimiserTargets",
)


__docformat__ = "restructuredtext en"
__all__ = ("SystemOptimiserTargets",)


Self = TypeVar("Self", bound="SystemOptimiserTargets")


class SystemOptimiserTargets(Enum):
    """SystemOptimiserTargets

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SYSTEM_OPTIMISER_TARGETS

    MINIMUM_FACE_WIDTH = 0
    MINIMUM_MASS = 1
    MINIMUM_WIDEST_FACE_WIDTH = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SystemOptimiserTargets.__setattr__ = __enum_setattr
SystemOptimiserTargets.__delattr__ = __enum_delattr
