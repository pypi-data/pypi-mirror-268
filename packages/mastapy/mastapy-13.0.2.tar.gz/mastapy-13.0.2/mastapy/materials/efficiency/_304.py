"""OilSealMaterialType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_OIL_SEAL_MATERIAL_TYPE = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "OilSealMaterialType"
)


__docformat__ = "restructuredtext en"
__all__ = ("OilSealMaterialType",)


Self = TypeVar("Self", bound="OilSealMaterialType")


class OilSealMaterialType(Enum):
    """OilSealMaterialType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OIL_SEAL_MATERIAL_TYPE

    VITON = 0
    BUNAN = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


OilSealMaterialType.__setattr__ = __enum_setattr
OilSealMaterialType.__delattr__ = __enum_delattr
