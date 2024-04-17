"""Range"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RANGE = python_net_import("SMT.MastaAPI.MathUtility", "Range")


__docformat__ = "restructuredtext en"
__all__ = ("Range",)


Self = TypeVar("Self", bound="Range")


class Range:
    """Range

    This is a mastapy class.
    """

    TYPE = _RANGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Range")

    class _Cast_Range:
        """Special nested class for casting Range to subclasses."""

        def __init__(self: "Range._Cast_Range", parent: "Range"):
            self._parent = parent

        @property
        def range(self: "Range._Cast_Range") -> "Range":
            return self._parent

        def __getattr__(self: "Range._Cast_Range", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Range.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1
        self._freeze()

    __frozen = False

    def __setattr__(self: Self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError(
                    ("Attempted to set unknown " "attribute: '{}'".format(attr))
                ) from None

            super().__setattr__(attr, value)

    def __delattr__(self: Self, name: str):
        raise AttributeError(
            "Cannot delete the attributes of a mastapy object."
        ) from None

    def _freeze(self: Self):
        self.__frozen = True

    @enforce_parameter_types
    def __eq__(self: Self, other: "Range") -> "bool":
        """bool

        Args:
            other (mastapy.math_utility.Range)
        """
        method_result = self.wrapped.op_Equality(
            self.wrapped, other.wrapped if other else None
        )
        return method_result

    @enforce_parameter_types
    def __ne__(self: Self, other: "Range") -> "bool":
        """bool

        Args:
            other (mastapy.math_utility.Range)
        """
        method_result = self.wrapped.op_Inequality(
            self.wrapped, other.wrapped if other else None
        )
        return method_result

    def __hash__(self: Self) -> "int":
        """int"""
        method_result = self.wrapped.GetHashCode()
        return method_result

    @property
    def cast_to(self: Self) -> "Range._Cast_Range":
        return self._Cast_Range(self)
