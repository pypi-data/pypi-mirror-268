"""TorqueSpecificationForSystemDeflection"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TORQUE_SPECIFICATION_FOR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueSpecificationForSystemDeflection",
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueSpecificationForSystemDeflection",)


Self = TypeVar("Self", bound="TorqueSpecificationForSystemDeflection")


class TorqueSpecificationForSystemDeflection(Enum):
    """TorqueSpecificationForSystemDeflection

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TORQUE_SPECIFICATION_FOR_SYSTEM_DEFLECTION

    CURRENT_TIME = 0
    SPECIFIED_ANGLE = 1
    SPECIFIED_TIME = 2
    MEAN = 3
    ROOT_MEAN_SQUARE = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TorqueSpecificationForSystemDeflection.__setattr__ = __enum_setattr
TorqueSpecificationForSystemDeflection.__delattr__ = __enum_delattr
