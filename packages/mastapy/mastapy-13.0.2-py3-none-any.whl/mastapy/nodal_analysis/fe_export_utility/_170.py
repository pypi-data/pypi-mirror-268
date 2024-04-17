"""FESubstructuringFileFormat"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURING_FILE_FORMAT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.FeExportUtility", "FESubstructuringFileFormat"
)


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructuringFileFormat",)


Self = TypeVar("Self", bound="FESubstructuringFileFormat")


class FESubstructuringFileFormat(Enum):
    """FESubstructuringFileFormat

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_SUBSTRUCTURING_FILE_FORMAT

    ANSYS_APDL_INPUT_FILE_OUTPUT_SUB = 0
    ANSYS_APDL_INPUT_FILE_OUTPUT_SUB_AND_TCMS = 1
    MSC_NASTRAN_BULK_DATA_FILE_OUTPUT_PCH = 2
    SIMCENTER_NASTRAN_BULK_DATA_FILE_OUTPUT_PCH = 3
    MSC_NASTRAN_BULK_DATA_FILE_OUTPUT_OP4_AND_PCH = 4
    SIMCENTER_NASTRAN_BULK_DATA_FILE_OUTPUT_OP4_AND_PCH = 5
    ABAQUS_INPUT_FILE_OUTPUT_MTX = 6
    ABAQUS_INPUT_FILE_OUTPUT_FIL = 7
    OPTISTRUCT_INPUT_FILE = 8


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FESubstructuringFileFormat.__setattr__ = __enum_setattr
FESubstructuringFileFormat.__delattr__ = __enum_delattr
