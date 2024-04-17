"""FluxBarrierStyle"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLUX_BARRIER_STYLE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "FluxBarrierStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FluxBarrierStyle",)


Self = TypeVar("Self", bound="FluxBarrierStyle")


class FluxBarrierStyle(Enum):
    """FluxBarrierStyle

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLUX_BARRIER_STYLE

    BRIDGE = 0
    CIRCULAR = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FluxBarrierStyle.__setattr__ = __enum_setattr
FluxBarrierStyle.__delattr__ = __enum_delattr
