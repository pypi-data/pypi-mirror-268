"""ElectricMachineDataImportType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DATA_IMPORT_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineDataImportType",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineDataImportType",)


Self = TypeVar("Self", bound="ElectricMachineDataImportType")


class ElectricMachineDataImportType(Enum):
    """ElectricMachineDataImportType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_DATA_IMPORT_TYPE

    MASTA = 0
    ALTAIR_FLUX = 1
    EXCEL = 2
    JMAG = 3
    MOTORCAD = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElectricMachineDataImportType.__setattr__ = __enum_setattr
ElectricMachineDataImportType.__delattr__ = __enum_delattr
