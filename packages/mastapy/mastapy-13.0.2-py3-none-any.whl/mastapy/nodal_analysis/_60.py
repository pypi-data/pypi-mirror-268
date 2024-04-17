"""FEMeshingOperation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_MESHING_OPERATION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEMeshingOperation"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEMeshingOperation",)


Self = TypeVar("Self", bound="FEMeshingOperation")


class FEMeshingOperation(Enum):
    """FEMeshingOperation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_MESHING_OPERATION

    SURFACE = 0
    VOLUME = 1
    CROSS_SECTION = 2
    CROSS_SECTION_TRIANGULATION = 3
    CROSS_SECTION_BOUNDARY = 4
    SURFACE_MESH_INPUT = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FEMeshingOperation.__setattr__ = __enum_setattr
FEMeshingOperation.__delattr__ = __enum_delattr
