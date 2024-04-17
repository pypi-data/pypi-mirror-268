"""MeshStiffnessModel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MESH_STIFFNESS_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel", "MeshStiffnessModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeshStiffnessModel",)


Self = TypeVar("Self", bound="MeshStiffnessModel")


class MeshStiffnessModel(Enum):
    """MeshStiffnessModel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MESH_STIFFNESS_MODEL

    CONSTANT_IN_LOA = 0
    ADVANCED_SYSTEM_DEFLECTION = 1
    ISO_SIMPLE_CONTINUOUS_MODEL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MeshStiffnessModel.__setattr__ = __enum_setattr
MeshStiffnessModel.__delattr__ = __enum_delattr
