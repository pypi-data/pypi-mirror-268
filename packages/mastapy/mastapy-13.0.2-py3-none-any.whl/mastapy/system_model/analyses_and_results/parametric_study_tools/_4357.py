"""DoeValueSpecificationOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DOE_VALUE_SPECIFICATION_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DoeValueSpecificationOption",
)


__docformat__ = "restructuredtext en"
__all__ = ("DoeValueSpecificationOption",)


Self = TypeVar("Self", bound="DoeValueSpecificationOption")


class DoeValueSpecificationOption(Enum):
    """DoeValueSpecificationOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DOE_VALUE_SPECIFICATION_OPTION

    ABSOLUTE = 0
    ADDITIVE = 1
    NORMAL_DISTRIBUTION = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DoeValueSpecificationOption.__setattr__ = __enum_setattr
DoeValueSpecificationOption.__delattr__ = __enum_delattr
