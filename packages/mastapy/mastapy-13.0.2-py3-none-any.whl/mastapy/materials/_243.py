"""AGMAMaterialApplications"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_MATERIAL_APPLICATIONS = python_net_import(
    "SMT.MastaAPI.Materials", "AGMAMaterialApplications"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAMaterialApplications",)


Self = TypeVar("Self", bound="AGMAMaterialApplications")


class AGMAMaterialApplications(Enum):
    """AGMAMaterialApplications

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_MATERIAL_APPLICATIONS

    GENERAL_APPLICATION = 0
    CRITICAL_SERVICE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMAMaterialApplications.__setattr__ = __enum_setattr
AGMAMaterialApplications.__delattr__ = __enum_delattr
