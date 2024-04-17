"""Optimisable"""

from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMISABLE = python_net_import("SMT.MastaAPI.MathUtility.Optimisation", "Optimisable")


__docformat__ = "restructuredtext en"
__all__ = ("Optimisable",)


Self = TypeVar("Self", bound="Optimisable")


class Optimisable(_1546.AbstractOptimisable):
    """Optimisable

    This is a mastapy class.
    """

    TYPE = _OPTIMISABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Optimisable")

    class _Cast_Optimisable:
        """Special nested class for casting Optimisable to subclasses."""

        def __init__(self: "Optimisable._Cast_Optimisable", parent: "Optimisable"):
            self._parent = parent

        @property
        def abstract_optimisable(
            self: "Optimisable._Cast_Optimisable",
        ) -> "_1546.AbstractOptimisable":
            return self._parent._cast(_1546.AbstractOptimisable)

        @property
        def optimisable(self: "Optimisable._Cast_Optimisable") -> "Optimisable":
            return self._parent

        def __getattr__(self: "Optimisable._Cast_Optimisable", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Optimisable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Optimisable._Cast_Optimisable":
        return self._Cast_Optimisable(self)
