"""FluxBarrierOrWeb"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLUX_BARRIER_OR_WEB = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "FluxBarrierOrWeb"
)


__docformat__ = "restructuredtext en"
__all__ = ("FluxBarrierOrWeb",)


Self = TypeVar("Self", bound="FluxBarrierOrWeb")


class FluxBarrierOrWeb(Enum):
    """FluxBarrierOrWeb

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLUX_BARRIER_OR_WEB

    FLUX_BARRIER = 0
    WEB = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FluxBarrierOrWeb.__setattr__ = __enum_setattr
FluxBarrierOrWeb.__delattr__ = __enum_delattr
