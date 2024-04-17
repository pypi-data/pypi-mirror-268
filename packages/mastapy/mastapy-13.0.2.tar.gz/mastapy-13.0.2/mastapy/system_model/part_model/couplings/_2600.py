"""RigidConnectorTiltStiffnessTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RIGID_CONNECTOR_TILT_STIFFNESS_TYPES = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RigidConnectorTiltStiffnessTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("RigidConnectorTiltStiffnessTypes",)


Self = TypeVar("Self", bound="RigidConnectorTiltStiffnessTypes")


class RigidConnectorTiltStiffnessTypes(Enum):
    """RigidConnectorTiltStiffnessTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RIGID_CONNECTOR_TILT_STIFFNESS_TYPES

    SINGLE_NODE_WITH_SPECIFIED_STIFFNESS = 0
    DERIVED_FROM_LENGTH_AND_RADIAL_STIFFNESS = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RigidConnectorTiltStiffnessTypes.__setattr__ = __enum_setattr
RigidConnectorTiltStiffnessTypes.__delattr__ = __enum_delattr
