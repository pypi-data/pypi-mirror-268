"""PlainGreaseFilledJournalBearingHousingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PLAIN_GREASE_FILLED_JOURNAL_BEARING_HOUSING_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm",
    "PlainGreaseFilledJournalBearingHousingType",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlainGreaseFilledJournalBearingHousingType",)


Self = TypeVar("Self", bound="PlainGreaseFilledJournalBearingHousingType")


class PlainGreaseFilledJournalBearingHousingType(Enum):
    """PlainGreaseFilledJournalBearingHousingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PLAIN_GREASE_FILLED_JOURNAL_BEARING_HOUSING_TYPE

    MACHINERY_ENCASED = 0
    PEDESTAL_BASE = 1
    CYLINDRICAL_HOUSING = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PlainGreaseFilledJournalBearingHousingType.__setattr__ = __enum_setattr
PlainGreaseFilledJournalBearingHousingType.__delattr__ = __enum_delattr
