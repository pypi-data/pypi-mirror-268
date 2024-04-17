"""PropertyTargetForDominantCandidateSearch"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PROPERTY_TARGET_FOR_DOMINANT_CANDIDATE_SEARCH = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "PropertyTargetForDominantCandidateSearch"
)


__docformat__ = "restructuredtext en"
__all__ = ("PropertyTargetForDominantCandidateSearch",)


Self = TypeVar("Self", bound="PropertyTargetForDominantCandidateSearch")


class PropertyTargetForDominantCandidateSearch(Enum):
    """PropertyTargetForDominantCandidateSearch

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PROPERTY_TARGET_FOR_DOMINANT_CANDIDATE_SEARCH

    MAXIMISE = 0
    MINIMISE = 1
    TARGET_VALUE = 2
    DO_NOT_INCLUDE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PropertyTargetForDominantCandidateSearch.__setattr__ = __enum_setattr
PropertyTargetForDominantCandidateSearch.__delattr__ = __enum_delattr
