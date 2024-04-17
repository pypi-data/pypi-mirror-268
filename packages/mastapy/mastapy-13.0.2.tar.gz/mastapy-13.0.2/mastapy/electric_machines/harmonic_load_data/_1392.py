"""StatorToothLoadInterpolator"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.electric_machines.harmonic_load_data import _1391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_TOOTH_LOAD_INTERPOLATOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "StatorToothLoadInterpolator"
)


__docformat__ = "restructuredtext en"
__all__ = ("StatorToothLoadInterpolator",)


Self = TypeVar("Self", bound="StatorToothLoadInterpolator")


class StatorToothLoadInterpolator(_1391.StatorToothInterpolator):
    """StatorToothLoadInterpolator

    This is a mastapy class.
    """

    TYPE = _STATOR_TOOTH_LOAD_INTERPOLATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorToothLoadInterpolator")

    class _Cast_StatorToothLoadInterpolator:
        """Special nested class for casting StatorToothLoadInterpolator to subclasses."""

        def __init__(
            self: "StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator",
            parent: "StatorToothLoadInterpolator",
        ):
            self._parent = parent

        @property
        def stator_tooth_interpolator(
            self: "StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator",
        ) -> "_1391.StatorToothInterpolator":
            return self._parent._cast(_1391.StatorToothInterpolator)

        @property
        def stator_tooth_load_interpolator(
            self: "StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator",
        ) -> "StatorToothLoadInterpolator":
            return self._parent

        def __getattr__(
            self: "StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorToothLoadInterpolator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spatial_force_absolute_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpatialForceAbsoluteTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_absolute_tolerance.setter
    @enforce_parameter_types
    def spatial_force_absolute_tolerance(self: Self, value: "float"):
        self.wrapped.SpatialForceAbsoluteTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def spatial_force_relative_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpatialForceRelativeTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_relative_tolerance.setter
    @enforce_parameter_types
    def spatial_force_relative_tolerance(self: Self, value: "float"):
        self.wrapped.SpatialForceRelativeTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator":
        return self._Cast_StatorToothLoadInterpolator(self)
