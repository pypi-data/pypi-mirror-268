"""ShavingSimulationCalculator"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "ShavingSimulationCalculator",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShavingSimulationCalculator",)


Self = TypeVar("Self", bound="ShavingSimulationCalculator")


class ShavingSimulationCalculator(_734.CutterSimulationCalc):
    """ShavingSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _SHAVING_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingSimulationCalculator")

    class _Cast_ShavingSimulationCalculator:
        """Special nested class for casting ShavingSimulationCalculator to subclasses."""

        def __init__(
            self: "ShavingSimulationCalculator._Cast_ShavingSimulationCalculator",
            parent: "ShavingSimulationCalculator",
        ):
            self._parent = parent

        @property
        def cutter_simulation_calc(
            self: "ShavingSimulationCalculator._Cast_ShavingSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def shaving_simulation_calculator(
            self: "ShavingSimulationCalculator._Cast_ShavingSimulationCalculator",
        ) -> "ShavingSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "ShavingSimulationCalculator._Cast_ShavingSimulationCalculator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cross_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrossAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_normal_shaving_pitch_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearNormalShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_transverse_shaving_pitch_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearTransverseShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def least_centre_distance_cross_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeastCentreDistanceCrossAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_transverse_shaving_pitch_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverTransverseShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaving_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShavingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_shaving_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalShavingContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingSimulationCalculator._Cast_ShavingSimulationCalculator":
        return self._Cast_ShavingSimulationCalculator(self)
