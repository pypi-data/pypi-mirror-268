"""TEExcitationType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TE_EXCITATION_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TEExcitationType"
)


__docformat__ = "restructuredtext en"
__all__ = ("TEExcitationType",)


Self = TypeVar("Self", bound="TEExcitationType")


class TEExcitationType(Enum):
    """TEExcitationType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TE_EXCITATION_TYPE

    TRANSMISSION_ERROR = 0
    MISALIGNMENT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TEExcitationType.__setattr__ = __enum_setattr
TEExcitationType.__delattr__ = __enum_delattr
