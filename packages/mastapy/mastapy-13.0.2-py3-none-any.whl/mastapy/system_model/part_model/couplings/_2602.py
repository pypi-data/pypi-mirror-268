"""RigidConnectorToothSpacingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RIGID_CONNECTOR_TOOTH_SPACING_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RigidConnectorToothSpacingType"
)


__docformat__ = "restructuredtext en"
__all__ = ("RigidConnectorToothSpacingType",)


Self = TypeVar("Self", bound="RigidConnectorToothSpacingType")


class RigidConnectorToothSpacingType(Enum):
    """RigidConnectorToothSpacingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RIGID_CONNECTOR_TOOTH_SPACING_TYPE

    EQUALLYSPACED_TEETH = 0
    CUSTOM_SPACING_OF_TEETH = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RigidConnectorToothSpacingType.__setattr__ = __enum_setattr
RigidConnectorToothSpacingType.__delattr__ = __enum_delattr
