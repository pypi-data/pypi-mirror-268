"""GearSetOptimisationResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISATION_RESULT = python_net_import(
    "SMT.MastaAPI.Gears", "GearSetOptimisationResult"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _954
    from mastapy.math_utility.optimisation import _1550
    from mastapy.gears.rating import _358


__docformat__ = "restructuredtext en"
__all__ = ("GearSetOptimisationResult",)


Self = TypeVar("Self", bound="GearSetOptimisationResult")


class GearSetOptimisationResult(_0.APIBase):
    """GearSetOptimisationResult

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISATION_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetOptimisationResult")

    class _Cast_GearSetOptimisationResult:
        """Special nested class for casting GearSetOptimisationResult to subclasses."""

        def __init__(
            self: "GearSetOptimisationResult._Cast_GearSetOptimisationResult",
            parent: "GearSetOptimisationResult",
        ):
            self._parent = parent

        @property
        def gear_set_optimisation_result(
            self: "GearSetOptimisationResult._Cast_GearSetOptimisationResult",
        ) -> "GearSetOptimisationResult":
            return self._parent

        def __getattr__(
            self: "GearSetOptimisationResult._Cast_GearSetOptimisationResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetOptimisationResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set(self: Self) -> "_954.GearSetDesign":
        """mastapy.gears.gear_designs.GearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_optimized(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsOptimized

        if temp is None:
            return False

        return temp

    @property
    def optimisation_history(self: Self) -> "_1550.OptimisationHistory":
        """mastapy.math_utility.optimisation.OptimisationHistory"""
        temp = self.wrapped.OptimisationHistory

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @optimisation_history.setter
    @enforce_parameter_types
    def optimisation_history(self: Self, value: "_1550.OptimisationHistory"):
        self.wrapped.OptimisationHistory = value.wrapped

    @property
    def rating(self: Self) -> "_358.AbstractGearSetRating":
        """mastapy.gears.rating.AbstractGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetOptimisationResult._Cast_GearSetOptimisationResult":
        return self._Cast_GearSetOptimisationResult(self)
