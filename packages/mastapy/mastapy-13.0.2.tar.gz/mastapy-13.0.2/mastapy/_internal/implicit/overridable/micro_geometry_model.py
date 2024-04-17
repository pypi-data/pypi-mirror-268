"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.gears import _340
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_MicroGeometryModel",)


Self = TypeVar("Self", bound="Overridable_MicroGeometryModel")


class Overridable_MicroGeometryModel(mixins.OverridableMixin, Enum):
    """Overridable_MicroGeometryModel

    A specific implementation of 'Overridable' for 'MicroGeometryModel' types.
    """

    __qualname__ = "MicroGeometryModel"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_340.MicroGeometryModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _340.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> "_340.MicroGeometryModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _340.MicroGeometryModel.type_()

    @property
    def value(self: Self) -> "_340.MicroGeometryModel":
        """mastapy.gears.MicroGeometryModel

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
    def override_value(self: Self) -> "_340.MicroGeometryModel":
        """mastapy.gears.MicroGeometryModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_340.MicroGeometryModel":
        """mastapy.gears.MicroGeometryModel

        Note:
            This property is readonly.
        """
        return None
