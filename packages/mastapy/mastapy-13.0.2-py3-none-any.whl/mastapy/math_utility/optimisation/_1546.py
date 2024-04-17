"""AbstractOptimisable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_OPTIMISABLE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "AbstractOptimisable"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1549


__docformat__ = "restructuredtext en"
__all__ = ("AbstractOptimisable",)


Self = TypeVar("Self", bound="AbstractOptimisable")


class AbstractOptimisable(_0.APIBase):
    """AbstractOptimisable

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_OPTIMISABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractOptimisable")

    class _Cast_AbstractOptimisable:
        """Special nested class for casting AbstractOptimisable to subclasses."""

        def __init__(
            self: "AbstractOptimisable._Cast_AbstractOptimisable",
            parent: "AbstractOptimisable",
        ):
            self._parent = parent

        @property
        def optimisable(
            self: "AbstractOptimisable._Cast_AbstractOptimisable",
        ) -> "_1549.Optimisable":
            from mastapy.math_utility.optimisation import _1549

            return self._parent._cast(_1549.Optimisable)

        @property
        def abstract_optimisable(
            self: "AbstractOptimisable._Cast_AbstractOptimisable",
        ) -> "AbstractOptimisable":
            return self._parent

        def __getattr__(
            self: "AbstractOptimisable._Cast_AbstractOptimisable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractOptimisable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def parameter_1(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Parameter1

        if temp is None:
            return 0.0

        return temp

    @parameter_1.setter
    @enforce_parameter_types
    def parameter_1(self: Self, value: "float"):
        self.wrapped.Parameter1 = float(value) if value is not None else 0.0

    @property
    def parameter_2(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Parameter2

        if temp is None:
            return 0.0

        return temp

    @parameter_2.setter
    @enforce_parameter_types
    def parameter_2(self: Self, value: "float"):
        self.wrapped.Parameter2 = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "AbstractOptimisable._Cast_AbstractOptimisable":
        return self._Cast_AbstractOptimisable(self)
