"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.bearings.bearing_designs.rolling import _2182
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_WidthSeries",)


Self = TypeVar("Self", bound="Overridable_WidthSeries")


class Overridable_WidthSeries(mixins.OverridableMixin, Enum):
    """Overridable_WidthSeries

    A specific implementation of 'Overridable' for 'WidthSeries' types.
    """

    __qualname__ = "WidthSeries"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_2182.WidthSeries":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2182.WidthSeries

    @classmethod
    def implicit_type(cls) -> "_2182.WidthSeries.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2182.WidthSeries.type_()

    @property
    def value(self: Self) -> "_2182.WidthSeries":
        """mastapy.bearings.bearing_designs.rolling.WidthSeries

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
    def override_value(self: Self) -> "_2182.WidthSeries":
        """mastapy.bearings.bearing_designs.rolling.WidthSeries

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_2182.WidthSeries":
        """mastapy.bearings.bearing_designs.rolling.WidthSeries

        Note:
            This property is readonly.
        """
        return None
