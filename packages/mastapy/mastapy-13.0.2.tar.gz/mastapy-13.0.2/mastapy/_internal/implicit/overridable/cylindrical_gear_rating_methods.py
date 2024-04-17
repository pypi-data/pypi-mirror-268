"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.materials import _254
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_CylindricalGearRatingMethods",)


Self = TypeVar("Self", bound="Overridable_CylindricalGearRatingMethods")


class Overridable_CylindricalGearRatingMethods(mixins.OverridableMixin, Enum):
    """Overridable_CylindricalGearRatingMethods

    A specific implementation of 'Overridable' for 'CylindricalGearRatingMethods' types.
    """

    __qualname__ = "CylindricalGearRatingMethods"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_254.CylindricalGearRatingMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _254.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> "_254.CylindricalGearRatingMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _254.CylindricalGearRatingMethods.type_()

    @property
    def value(self: Self) -> "_254.CylindricalGearRatingMethods":
        """mastapy.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        return None

    @property
    def override_value(self: Self) -> "_254.CylindricalGearRatingMethods":
        """mastapy.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_254.CylindricalGearRatingMethods":
        """mastapy.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        return None
