"""StatorToothMomentInterpolator"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.electric_machines.harmonic_load_data import _1391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_TOOTH_MOMENT_INTERPOLATOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "StatorToothMomentInterpolator"
)


__docformat__ = "restructuredtext en"
__all__ = ("StatorToothMomentInterpolator",)


Self = TypeVar("Self", bound="StatorToothMomentInterpolator")


class StatorToothMomentInterpolator(_1391.StatorToothInterpolator):
    """StatorToothMomentInterpolator

    This is a mastapy class.
    """

    TYPE = _STATOR_TOOTH_MOMENT_INTERPOLATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorToothMomentInterpolator")

    class _Cast_StatorToothMomentInterpolator:
        """Special nested class for casting StatorToothMomentInterpolator to subclasses."""

        def __init__(
            self: "StatorToothMomentInterpolator._Cast_StatorToothMomentInterpolator",
            parent: "StatorToothMomentInterpolator",
        ):
            self._parent = parent

        @property
        def stator_tooth_interpolator(
            self: "StatorToothMomentInterpolator._Cast_StatorToothMomentInterpolator",
        ) -> "_1391.StatorToothInterpolator":
            return self._parent._cast(_1391.StatorToothInterpolator)

        @property
        def stator_tooth_moment_interpolator(
            self: "StatorToothMomentInterpolator._Cast_StatorToothMomentInterpolator",
        ) -> "StatorToothMomentInterpolator":
            return self._parent

        def __getattr__(
            self: "StatorToothMomentInterpolator._Cast_StatorToothMomentInterpolator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorToothMomentInterpolator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spatial_moment_absolute_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpatialMomentAbsoluteTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_moment_absolute_tolerance.setter
    @enforce_parameter_types
    def spatial_moment_absolute_tolerance(self: Self, value: "float"):
        self.wrapped.SpatialMomentAbsoluteTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def spatial_moment_relative_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpatialMomentRelativeTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_moment_relative_tolerance.setter
    @enforce_parameter_types
    def spatial_moment_relative_tolerance(self: Self, value: "float"):
        self.wrapped.SpatialMomentRelativeTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "StatorToothMomentInterpolator._Cast_StatorToothMomentInterpolator":
        return self._Cast_StatorToothMomentInterpolator(self)
