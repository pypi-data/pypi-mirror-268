"""ParetoOptimisationFilter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_FILTER = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationFilter"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationFilter",)


Self = TypeVar("Self", bound="ParetoOptimisationFilter")


class ParetoOptimisationFilter(_0.APIBase):
    """ParetoOptimisationFilter

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_FILTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationFilter")

    class _Cast_ParetoOptimisationFilter:
        """Special nested class for casting ParetoOptimisationFilter to subclasses."""

        def __init__(
            self: "ParetoOptimisationFilter._Cast_ParetoOptimisationFilter",
            parent: "ParetoOptimisationFilter",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_filter(
            self: "ParetoOptimisationFilter._Cast_ParetoOptimisationFilter",
        ) -> "ParetoOptimisationFilter":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationFilter._Cast_ParetoOptimisationFilter", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationFilter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def filter_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.FilterRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @filter_range.setter
    @enforce_parameter_types
    def filter_range(self: Self, value: "_1496.Range"):
        self.wrapped.FilterRange = value.wrapped

    @property
    def property_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Property

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationFilter._Cast_ParetoOptimisationFilter":
        return self._Cast_ParetoOptimisationFilter(self)
