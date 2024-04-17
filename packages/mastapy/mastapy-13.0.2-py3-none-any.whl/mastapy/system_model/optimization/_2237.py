"""CylindricalGearOptimizationStep"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.optimization import _2240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_OPTIMIZATION_STEP = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "CylindricalGearOptimizationStep"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearOptimizationStep",)


Self = TypeVar("Self", bound="CylindricalGearOptimizationStep")


class CylindricalGearOptimizationStep(_2240.OptimizationStep):
    """CylindricalGearOptimizationStep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_OPTIMIZATION_STEP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearOptimizationStep")

    class _Cast_CylindricalGearOptimizationStep:
        """Special nested class for casting CylindricalGearOptimizationStep to subclasses."""

        def __init__(
            self: "CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep",
            parent: "CylindricalGearOptimizationStep",
        ):
            self._parent = parent

        @property
        def optimization_step(
            self: "CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep",
        ) -> "_2240.OptimizationStep":
            return self._parent._cast(_2240.OptimizationStep)

        @property
        def cylindrical_gear_optimization_step(
            self: "CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep",
        ) -> "CylindricalGearOptimizationStep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearOptimizationStep.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_extended_tip_contact(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeExtendedTipContact

        if temp is None:
            return False

        return temp

    @include_extended_tip_contact.setter
    @enforce_parameter_types
    def include_extended_tip_contact(self: Self, value: "bool"):
        self.wrapped.IncludeExtendedTipContact = (
            bool(value) if value is not None else False
        )

    @property
    def include_tip_edge_stresses(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTipEdgeStresses

        if temp is None:
            return False

        return temp

    @include_tip_edge_stresses.setter
    @enforce_parameter_types
    def include_tip_edge_stresses(self: Self, value: "bool"):
        self.wrapped.IncludeTipEdgeStresses = (
            bool(value) if value is not None else False
        )

    @property
    def use_advanced_ltca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedLTCA

        if temp is None:
            return False

        return temp

    @use_advanced_ltca.setter
    @enforce_parameter_types
    def use_advanced_ltca(self: Self, value: "bool"):
        self.wrapped.UseAdvancedLTCA = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep":
        return self._Cast_CylindricalGearOptimizationStep(self)
