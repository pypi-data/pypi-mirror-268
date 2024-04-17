"""PlanetaryRatingLoadSharingOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PLANETARY_RATING_LOAD_SHARING_OPTION = python_net_import(
    "SMT.MastaAPI.Gears", "PlanetaryRatingLoadSharingOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryRatingLoadSharingOption",)


Self = TypeVar("Self", bound="PlanetaryRatingLoadSharingOption")


class PlanetaryRatingLoadSharingOption(Enum):
    """PlanetaryRatingLoadSharingOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PLANETARY_RATING_LOAD_SHARING_OPTION

    ANALYSIS_RESULTS = 0
    DISTRIBUTED_TO_GIVE_WORST_DAMAGE = 1
    SINGLE_PLANET_TAKING_PEAK_LOAD_OTHER_PLANETS_TAKING_EQUAL_LOAD = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PlanetaryRatingLoadSharingOption.__setattr__ = __enum_setattr
PlanetaryRatingLoadSharingOption.__delattr__ = __enum_delattr
