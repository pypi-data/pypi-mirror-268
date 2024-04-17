"""ModelSplittingMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MODEL_SPLITTING_METHOD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "ModelSplittingMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("ModelSplittingMethod",)


Self = TypeVar("Self", bound="ModelSplittingMethod")


class ModelSplittingMethod(Enum):
    """ModelSplittingMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MODEL_SPLITTING_METHOD

    NONE = 0
    ELEMENT_PROPERTY_ID = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ModelSplittingMethod.__setattr__ = __enum_setattr
ModelSplittingMethod.__delattr__ = __enum_delattr
