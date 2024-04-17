"""MeshStiffnessSource"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MESH_STIFFNESS_SOURCE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MeshStiffnessSource"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeshStiffnessSource",)


Self = TypeVar("Self", bound="MeshStiffnessSource")


class MeshStiffnessSource(Enum):
    """MeshStiffnessSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MESH_STIFFNESS_SOURCE

    HARMONIC_EXCITATION_TYPE = 0
    SYSTEM_DEFLECTION = 1
    BASIC_LTCA = 2
    ADVANCED_LTCA = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MeshStiffnessSource.__setattr__ = __enum_setattr
MeshStiffnessSource.__delattr__ = __enum_delattr
