"""ShaftDiameterModificationDueToRollingBearingRing"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SHAFT_DIAMETER_MODIFICATION_DUE_TO_ROLLING_BEARING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel",
    "ShaftDiameterModificationDueToRollingBearingRing",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDiameterModificationDueToRollingBearingRing",)


Self = TypeVar("Self", bound="ShaftDiameterModificationDueToRollingBearingRing")


class ShaftDiameterModificationDueToRollingBearingRing(Enum):
    """ShaftDiameterModificationDueToRollingBearingRing

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SHAFT_DIAMETER_MODIFICATION_DUE_TO_ROLLING_BEARING_RING

    PRESERVE_RING_MASS = 0
    USE_RACE_DIAMETER = 1
    IGNORE_BEARING_RING = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ShaftDiameterModificationDueToRollingBearingRing.__setattr__ = __enum_setattr
ShaftDiameterModificationDueToRollingBearingRing.__delattr__ = __enum_delattr
