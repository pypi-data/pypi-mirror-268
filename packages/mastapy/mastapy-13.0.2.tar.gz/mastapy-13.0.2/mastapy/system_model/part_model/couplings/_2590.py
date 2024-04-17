"""ConceptCouplingHalfPositioning"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_POSITIONING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalfPositioning"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfPositioning",)


Self = TypeVar("Self", bound="ConceptCouplingHalfPositioning")


class ConceptCouplingHalfPositioning(Enum):
    """ConceptCouplingHalfPositioning

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONCEPT_COUPLING_HALF_POSITIONING

    HALVES_ARE_COINCIDENT = 0
    HALVES_ARE_CONCENTRIC = 1
    HALVES_FREELY_POSITIONED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ConceptCouplingHalfPositioning.__setattr__ = __enum_setattr
ConceptCouplingHalfPositioning.__delattr__ = __enum_delattr
