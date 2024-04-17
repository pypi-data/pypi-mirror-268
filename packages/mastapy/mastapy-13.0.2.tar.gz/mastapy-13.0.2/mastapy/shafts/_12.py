"""FkmSnCurveModel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FKM_SN_CURVE_MODEL = python_net_import("SMT.MastaAPI.Shafts", "FkmSnCurveModel")


__docformat__ = "restructuredtext en"
__all__ = ("FkmSnCurveModel",)


Self = TypeVar("Self", bound="FkmSnCurveModel")


class FkmSnCurveModel(Enum):
    """FkmSnCurveModel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FKM_SN_CURVE_MODEL

    MODEL_I = 0
    MODEL_II = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FkmSnCurveModel.__setattr__ = __enum_setattr
FkmSnCurveModel.__delattr__ = __enum_delattr
