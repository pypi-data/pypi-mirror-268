"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _513
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_HelicalGearMicroGeometryOption",)


Self = TypeVar("Self", bound="Overridable_HelicalGearMicroGeometryOption")


class Overridable_HelicalGearMicroGeometryOption(mixins.OverridableMixin, Enum):
    """Overridable_HelicalGearMicroGeometryOption

    A specific implementation of 'Overridable' for 'HelicalGearMicroGeometryOption' types.
    """

    __qualname__ = "HelicalGearMicroGeometryOption"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_513.HelicalGearMicroGeometryOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _513.HelicalGearMicroGeometryOption

    @classmethod
    def implicit_type(cls) -> "_513.HelicalGearMicroGeometryOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _513.HelicalGearMicroGeometryOption.type_()

    @property
    def value(self: Self) -> "_513.HelicalGearMicroGeometryOption":
        """mastapy.gears.rating.cylindrical.iso6336.HelicalGearMicroGeometryOption

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
    def override_value(self: Self) -> "_513.HelicalGearMicroGeometryOption":
        """mastapy.gears.rating.cylindrical.iso6336.HelicalGearMicroGeometryOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_513.HelicalGearMicroGeometryOption":
        """mastapy.gears.rating.cylindrical.iso6336.HelicalGearMicroGeometryOption

        Note:
            This property is readonly.
        """
        return None
