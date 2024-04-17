"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.bearings.bearing_designs.rolling import _2158
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_DiameterSeries",)


Self = TypeVar("Self", bound="Overridable_DiameterSeries")


class Overridable_DiameterSeries(mixins.OverridableMixin, Enum):
    """Overridable_DiameterSeries

    A specific implementation of 'Overridable' for 'DiameterSeries' types.
    """

    __qualname__ = "DiameterSeries"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_2158.DiameterSeries":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2158.DiameterSeries

    @classmethod
    def implicit_type(cls) -> "_2158.DiameterSeries.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2158.DiameterSeries.type_()

    @property
    def value(self: Self) -> "_2158.DiameterSeries":
        """mastapy.bearings.bearing_designs.rolling.DiameterSeries

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
    def override_value(self: Self) -> "_2158.DiameterSeries":
        """mastapy.bearings.bearing_designs.rolling.DiameterSeries

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_2158.DiameterSeries":
        """mastapy.bearings.bearing_designs.rolling.DiameterSeries

        Note:
            This property is readonly.
        """
        return None
