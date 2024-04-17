"""CoordinateSystemForWhine"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_FOR_WHINE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CoordinateSystemForWhine",
)


__docformat__ = "restructuredtext en"
__all__ = ("CoordinateSystemForWhine",)


Self = TypeVar("Self", bound="CoordinateSystemForWhine")


class CoordinateSystemForWhine(Enum):
    """CoordinateSystemForWhine

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COORDINATE_SYSTEM_FOR_WHINE

    LOCAL_COORDINATE_SYSTEM = 0
    GLOBAL_COORDINATE_SYSTEM = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CoordinateSystemForWhine.__setattr__ = __enum_setattr
CoordinateSystemForWhine.__delattr__ = __enum_delattr
