"""ImportType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_IMPORT_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ImportType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ImportType",)


Self = TypeVar("Self", bound="ImportType")


class ImportType(Enum):
    """ImportType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _IMPORT_TYPE

    DUTY_CYCLE_TIME_SERIES = 0
    INDIVIDUAL_LOAD_CASE = 1
    INDIVIDUAL_LOAD_CASES_AS_TIME_SERIES = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ImportType.__setattr__ = __enum_setattr
ImportType.__delattr__ = __enum_delattr
