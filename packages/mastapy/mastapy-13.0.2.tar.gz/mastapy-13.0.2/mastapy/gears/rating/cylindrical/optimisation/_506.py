"""SafetyFactorOptimisationResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationResults",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.optimisation import _507


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationResults",)


Self = TypeVar("Self", bound="SafetyFactorOptimisationResults")
T = TypeVar("T", bound="_507.SafetyFactorOptimisationStepResult")


class SafetyFactorOptimisationResults(_0.APIBase, Generic[T]):
    """SafetyFactorOptimisationResults

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorOptimisationResults")

    class _Cast_SafetyFactorOptimisationResults:
        """Special nested class for casting SafetyFactorOptimisationResults to subclasses."""

        def __init__(
            self: "SafetyFactorOptimisationResults._Cast_SafetyFactorOptimisationResults",
            parent: "SafetyFactorOptimisationResults",
        ):
            self._parent = parent

        @property
        def safety_factor_optimisation_results(
            self: "SafetyFactorOptimisationResults._Cast_SafetyFactorOptimisationResults",
        ) -> "SafetyFactorOptimisationResults":
            return self._parent

        def __getattr__(
            self: "SafetyFactorOptimisationResults._Cast_SafetyFactorOptimisationResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SafetyFactorOptimisationResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def values(self: Self) -> "List[T]":
        """List[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SafetyFactorOptimisationResults._Cast_SafetyFactorOptimisationResults":
        return self._Cast_SafetyFactorOptimisationResults(self)
