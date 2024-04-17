"""SplineFixtureTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPLINE_FIXTURE_TYPES = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SplineFixtureTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("SplineFixtureTypes",)


Self = TypeVar("Self", bound="SplineFixtureTypes")


class SplineFixtureTypes(Enum):
    """SplineFixtureTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPLINE_FIXTURE_TYPES

    FLEXIBLE = 0
    FIXED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SplineFixtureTypes.__setattr__ = __enum_setattr
SplineFixtureTypes.__delattr__ = __enum_delattr
