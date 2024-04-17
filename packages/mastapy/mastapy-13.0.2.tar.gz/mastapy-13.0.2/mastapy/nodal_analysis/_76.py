"""MeshingDiameterForGear"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MESHING_DIAMETER_FOR_GEAR = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "MeshingDiameterForGear"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeshingDiameterForGear",)


Self = TypeVar("Self", bound="MeshingDiameterForGear")


class MeshingDiameterForGear(Enum):
    """MeshingDiameterForGear

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MESHING_DIAMETER_FOR_GEAR

    ROOT_DIAMETER = 0
    TIP_DIAMETER = 1
    REFERENCE_DIAMETER = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MeshingDiameterForGear.__setattr__ = __enum_setattr
MeshingDiameterForGear.__delattr__ = __enum_delattr
